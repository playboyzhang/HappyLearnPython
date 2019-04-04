# 假定你的老板用电子邮件发给你上千个文件，文件名包含美国风格的日期
# （MM-DD-YYYY），需要将它们改名为欧洲风格的日期（DD-MM-YYYY）。手工 完
# 成这个无聊的任务可能需要几天时间！让我们写一个程序来完成它。
# 下面是程序要做的事：
# • 检查当前工作目录的所有文件名， 寻找美国风格的日期。
# • 如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格。
# 这意味着代码需要做下面的事情：
# • 创建一个正则表达式， 可以识别美国风格日期的文本模式。
# • 调用 os.listdir()，找出工作目录中的所有文件。
# • 循环遍历每个文件名， 利用该正则表达式检查它是否包含日期。
# • 如果它包含日期，用 shutil.move()对该文件改名。
# 对于这个项目， 打开一个新的文件编辑器窗口， 将代码保存为 renameDates.py。
import shutil,os,re
# Create a regex that metches files with the American date format
datePattern = re.compile(r"""^(.*?)   #all text before the date
               ((0|1)?\d)-       #one or two digits for the month 
               ((0|1|2|3)?\d)-  #one or two digits for the day 
               ((19|20)\d\d) # four digits for the year
               (.*?)$ # all text after the date
""",re.VERBOSE)

# TODO: Loop over the files in the working directory.
# TODO: Skip files without a date.
# TODO: Get the different parts of the filename.
# TODO: Form the European-style filename.
# TODO: Get the full, absolute file paths.
# TODO: Rename the files.

#Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    #Skip files without a date
    if mo == None:
        continue
    #Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)


    #From the uropean-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' +yearPart + afterPart


    #Get the full,absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)


    #rename the files.
    print('Renaming "%s to "%s" ... ' %(amerFilename,euroFilename))
    # shutil.move(amerFilename,euroFilename)  #uncomment after testing