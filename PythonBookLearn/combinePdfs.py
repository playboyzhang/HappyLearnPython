# 假定你有一个很无聊的任务，需要将几十个 PDF 文件合并成一个 PDF 文件。 每
# 一个文件都有一个封面作为第一页，但你不希望合并后的文件中重复出现这些封
# 面。即使有许多免费的程序可以合并 PDF，很多也只是简单的将文件合并在一起。
# 让我们来写一个 Python 程序，定制需要合并到 PDF 中的页面。
# 总的来说，该程序需要完成：
#  找到当前工作目录中所有 PDF 文件。
#  按文件名排序，这样就能有序地添加这些 PDF。
#  除了第一页之外，将每个 PDF 的所有页面写入输出的文件。
# 从实现的角度来看，代码需要完成下列任务：
#  调用 os.listdir()，找到当前工作目录中的所有文件，去除掉非 PDF 文件。
#  调用 Python 的 sort()列表方法，对文件名按字母排序。
#  为输出的 PDF 文件创建 PdfFileWriter 对象。
#  循环遍历每个 PDF 文件， 为它创建 PdfFileReader 对象。
#  针对每个 PDF 文件，循环遍历每一页，第一页除外。
#  将页面添加到输出的 PDF。
#  将输出的 PDF 写入一个文件，名为 allminutes.pdf。
# 针对这个项目，打开一个新的文件编辑器窗口，将它保存为 combinePdfs.py。

#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF.

import PyPDF2,os

#get all the pdf filenames.

pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# TODO: Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # TODO: Loop through all the pages (except the first) and add them.
    for pageNum in range(1,pdfReader.numPages):                #默认0为第一页，因为要跳过第一页所以从1开始循环
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# TODO: Save the resulting PDF to a file.

pdfOutput = open('allminutes.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()




