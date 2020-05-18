import os
import glob

count = 0


def ds_compare(files1, files2):

    for x in range(len(files1)):
        files1[x] = os.path.basename(files1[x])

    for y in range(len(files2)):
        files2[y] = os.path.basename(files2[y])

    files1.sort()
    files2.sort()

    print('Folder 1 = ', len(files1), '  Folder 2 = ', len(files2))

    for z in range(len(files1)):
        if ('opened_proc_gt_' + files1[z]) != (files2[z]):
            print(files1[z], '  ', files2[z])
            print(z, ')  Mismatch at ', files1, '  ', files2)


folder1 = glob.glob('/home/weaver/PycharmProjects/datasets/gradSet/leftImg8bit/**/*.png', recursive=True)
folder2 = glob.glob('/home/weaver/PycharmProjects/datasets/gradSet/gtFine/**/*.png', recursive=True)
ds_compare(folder1, folder2)