import os

# 假定的学生名单
student_names = [
    "陈德杯", "王祥乐", "李宽", "赵冠淞", "杨凯", "郑皓原", "陈舜迪", "陈天宇", "余志恒", "黄奕菲",
    "罗淞译", "邱叙涵", "潘海柱", "应睿锋", "李文杰", "蔡紫莹", "邢塬", "张佳宁", "潘阳", "传游",
    "许扬浩", "韩宇飞", "潘宇轩", "于凌轩", "谈锐", "黄依婷", "王振业", "李煜", "徐子璠", "骆星源",
    "王子歌", "王振乾", "郑权", "李亚楠", "黄梓翀", "王宇卓", "范晗霖"
]

# 假定的文件目录路径
directory_path = r'E:\Download\网安实验6'

# 这个函数将检查每个学生的作业是否在目录中
def check_assignments(directory, students):
    # 获取目录下的所有文件名
    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        return "The directory path provided does not exist."

    # 未提交作业的学生名单
    students_not_submitted = []

    # 检查每个学生的作业是否已提交
    for student in students:
        # 如果学生名字不在文件名中，添加到未提交名单中
        if not any(student in file for file in files):
            students_not_submitted.append(student)

    return students_not_submitted

students_not_submitted = check_assignments(directory_path, student_names)
print(students_not_submitted,end='\n')

for student in students_not_submitted:
    # 对下面的student固定长度
    print(f"{student:<8}未提交作业。")
