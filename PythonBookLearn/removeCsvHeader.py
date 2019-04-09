# 假设你有一个枯燥的任务，要删除几百 CSV 文件的第一行。也许你会将它们送入一
# 个自动化的过程，只需要数据，不需要每列顶部的表头。可以在 Excel 中打开每个文件，
# 删除第一行，并重新保存该文件，但这需要几个小时。让我们写一个程序来做这件事。
# 该程序需要打开当前工作目录中所有扩展名为.csv 的文件，读取 CSV 文件的内
# 容，并除掉第一行的内容重新写入同名的文件。这将用新的、无表头的内容替换
# CSV 文件的旧内容。
# 总的来说，该程序必须做到以下几点：
# • 找出当前工作目录中的所有 CSV 文件。
# • 读取每个文件的全部内容。
# • 跳过第一行，将内容写入一个新的 CSV 文件。
# 在代码层面上，这意味着该程序需要做到以下几点：
# • 循环遍历从 os.listdir()得到的文件列表，跳过非 CSV 文件。
# • 创建一个 CSV Reader 对象，读取该文件的内容，利用 line_num 属性确定要跳
# 过哪一行。
# • 创建一个 CSV Writer 对象，将读入的数据写入新文件。
# 针对这个项目，打开一个新的文件编辑器窗口，并保存为 removeCsvHeader.py。

#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.


import csv,os

os.makedirs('headerRemoved',exist_ok=True)

# Loop through every file in the current working directory

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue   #skip non-csv files

    print('Removing header from ' +csvFilename +'...')


    #TODO: Read the CSV file in （skipping first row).

    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num ==1:
            continue     #skip first now
        csvRows.append(row)

    csvFileObj.close()

    #TODO: Write out the CSV file.

    csvFileObj = open(os.path.join('headerRemoved',csvFilename),'w',newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()


