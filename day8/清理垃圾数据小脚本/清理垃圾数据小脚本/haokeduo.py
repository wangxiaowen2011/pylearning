# -*- coding: gbk -*-
def ReadRow():
    '''
    #����������
    #����һ
    # L = []
    # with open('test.txt','r') as f:
    #     f=f.decode()
    #     for line in f.readlines():
    #         L.append(line.strip('\n'))
    '''

    # �����Ե�����
    # ������
    import xlrd, xlwt  # �����дģ��
    wbk = xlrd.open_workbook(u'Testdata2.xls')  # �򿪹����ļ�
    SheetName = wbk.sheet_names()  # ��ȡ����������
    l = []
    L = []
    for sheet_name in SheetName:
        SheetRow = wbk.sheet_by_name(sheet_name)  # ��ȡ��������
        TableRow = SheetRow.nrows, SheetRow.ncols  # ͳ�ƹ���������
        for i in range(TableRow[0]):  # ѭ��ÿһ��
            Rows1 = SheetRow.row_values(i)  # ��ȡ��һ��
            l.append(Rows1)  # ׷�ӵ����б�
        break
    for z in l:#ѭ���б�
        for q in range(TableRow[1]):
            L.append(z[q])

    # ����Ҫ�޸ĵ�����
    workbook1 = xlrd.open_workbook(u'haokeduo.xls')  # ���ļ�
    sheet_names = workbook1.sheet_names()  # �򿪵Ĺ���������
    row_list = []#������б�
    L = [x for x in L if x != '']  # �����б�ɾ�����ַ���
    for sheet_name in sheet_names:
        sheet2 = workbook1.sheet_by_name(sheet_name)  # ��ȡ��������
        table = sheet2.nrows, sheet2.ncols  # ͳ�ƹ���������
        wb = xlwt.Workbook()  # ����excel
        ws = wb.add_sheet(u'�ÿζർ�����')  # ������������
        for i in range(table[0]):  # ѭ��ÿһ��
            rows1 = sheet2.row_values(i)  # ��ȡ��һ����
            union = list(set(L) & set(rows1))  # ȡ�����б�Ľ���
            if union:  # �жϽ����Ƿ�Ϊ��
                continue  # ����
            else:
                row_list.append(rows1)  # ׷�ӵ����б�
        break

    # ����д���˺������
    w = 0  # ������excel���г�ʼֵ
    for z in row_list:  # ѭ�����б����ݸ�ֵ������
        for q in range(table[1]):  # ��ȡÿ��
            if type(z[q]) == float:  # �ж��е�ֵ�Ƿ�Ϊ������
                ws.write(w, q, int(z[q]))  # ת��������
            else:
                ws.write(w, q, str(z[q]))  # ֱ��д����Ԫ��

        w += 1  # ����+1
    wb.save('XGhaokeduo.xls')#����Ϊ�µ��ļ�


def SJ():#��װ�Ĳ鿴����ʱ��
    import time
    start = time.time()
    ReadRow()
    end = time.time()
    print(end - start)


SJ()
