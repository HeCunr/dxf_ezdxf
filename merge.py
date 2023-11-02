import ezdxf

# 定义一个函数，用于删除指定类型的实体
def delete_entities_by_type(filename, entity_types_to_delete):
    # 从文件加载DXF文档
    doc = ezdxf.readfile(filename)

    # 删除所有图层中的指定类型的实体
    for layer in doc.modelspace().query('LAYER'):
        layer_name = layer.dxf.name
        for entity in layer.query('*'):
            entity_type = entity.dxftype()
            if entity_type in entity_types_to_delete:
                entity.destroy()

    # 删除所有块中的指定类型的实体
    block_definitions = doc.blocks
    for block in block_definitions:
        for entity in block.query('*'):
            entity_type = entity.dxftype()
            if entity_type in entity_types_to_delete:
                entity.destroy()

    # 删除名为"FR"的块中的所有实体
    if "FR" in block_definitions:
        fr_block = block_definitions.get("FR")
        if fr_block is not None:
            for entity in fr_block.query('*'):
                entity.destroy()

    # 保存修改后的DXF文件
    doc.saveas(filename)

# 定义一个函数，用于删除指定的DXF文件中的指定图层上的指定类型的实体
def delete_entities(filename, layer_name_to_delete, entity_types_to_delete):
    # 从文件加载DXF文档
    doc = ezdxf.readfile(filename)

    # 获取文档中的图层列表
    layers = doc.layers

    # 遍历图层列表，查找要删除的图层
    for layer in layers:
        if layer.dxf.name == layer_name_to_delete:
            # 找到要删除的图层后，继续查找文档中与该图层相关的实体

            # 获取文档模型空间（modelspace）
            modelspace = doc.modelspace()

            # 使用查询语句查找与指定图层相关的实体
            for entity in modelspace.query('*[layer=="' + layer_name_to_delete + '"]'):
                # 检查实体类型
                entity_type = entity.dxftype()

                # 删除指定类型的实体
                if entity_type in entity_types_to_delete:
                    entity.destroy()

    # 保存修改后的DXF文件
    doc.saveas(filename)

# 指定要删除的实体类型列表
entity_types_to_delete = ["TEXT", "LEADER", "DIMENSION", "MTEXT", "MULTILEADER"]

# 调用函数来删除DXF文件中所有图层和块上的指定类型的实体
delete_entities_by_type("C:\\DWF\\origin2.dxf", entity_types_to_delete)

# 删除名为"TB"图层上的"LINE"实体
delete_entities("C:\\DWF\\origin2.dxf", "TB", ["LINE"])

# 删除名为"1D"图层上的"LINE"实体
delete_entities("C:\\DWF\\origin2.dxf", "1D", ["LINE"])
