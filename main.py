import ezdxf

# 定义一个函数，用于删除指定类型的实体
def delete_entities_by_type(filename, entity_types_to_delete):
    # 从文件加载DXF文档
    doc = ezdxf.readfile(filename)

    # 获取文档中的模型空间（Modelspace）
    modelspace = doc.modelspace()

    # 遍历模型空间中的所有实体
    for entity in modelspace.query('*'):
        # 检查实体类型
        entity_type = entity.dxftype()

        # 如果实体类型在要删除的列表中，则删除该实体
        if entity_type in entity_types_to_delete:
            entity.destroy()

    # 获取文档中的所有块定义
    block_definitions = doc.blocks

    # 遍历所有块定义
    for block in block_definitions:
        # 遍历块中的所有实体
        for entity in block.query('*'):
            entity_type = entity.dxftype()

            # 如果实体类型在要删除的列表中，则删除该实体
            if entity_type in entity_types_to_delete:
                entity.destroy()

    # 保存修改后的DXF文件
    doc.saveas(filename)

# 指定要删除的实体类型列表
entity_types_to_delete = ["TEXT", "LEADER", "DIMENSION", "MTEXT", "MULTILEADER"]

# 调用函数来删除DXF文件中所有图层和块上的指定类型的实体
delete_entities_by_type("C:\\DWF\\DFN8LBH(No TAPE)-483 Rev1_u.dxf", entity_types_to_delete)
