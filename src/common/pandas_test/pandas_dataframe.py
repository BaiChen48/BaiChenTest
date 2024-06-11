# 导入Pandas库
import pandas as pd

# 构建DataFrame，其中index、dtype和columns是可选项,
dataFrame = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], index=["第一行", "第二行"],
                         columns=["第一列", "第二列", "第三列"])
# 切片 切行
# 切片,常规切片只能切行，要想切列，就得使用loc和iloc，loc使用索引和列名切，iloc使用行号和列号切
# print(dataFrame[0:3])
# # 切列
# print(dataFrame.loc['第一行'])
#
# print(dataFrame.loc[::, '第一列'])
#
# print(dataFrame.loc['第二行', '第二列'])

print(dataFrame.iloc[1,1])

# 新增列
dataFrame["新增列"] = 6
# 新增行
dataFrame.loc["c"] = [55,88,99,66]
print(dataFrame,end='\t')

#
# 删除可以分好几种，下面一一介绍
# 删除行
dataFrame.drop(index="c",inplace=True)

# 删除列,注意这里的0是列名哦
dataFrame.drop(columns=0,inplace=True)

# 删除nan值,参数axis指定删除行还是列，0代表行，1代表列
#	how指定是有一个旧删除，还是所有都为nan值菜删除，可选值'any', 'all'
# 	thresh阈值，指定行或者列超过指定的个数旧删除
# 	inplace是否在源数据删除，True代表是，False代表否

dataFrame.dropna(inplace=True)

# 删除重复值
# 参数subset: 指定去重依据，多条件用[]括起来
#    keep: 保留第一个还是最后一个，默认第一个，可选值first、last
#     inplace:是否在源数据删除
dataFrame.drop_duplicates()


# 前N行,不写参数N，则是前五行
dataFrame.head()

# 后N行,不写参数N，则是后五行
dataFrame.tail()

# 总体信息,包括索引，各列类型，整体数据类型，内存大小等信息
print(dataFrame.info())

if __name__ == '__main__':
    pass
    # print(dataFrame)
