# -*- coding: utf-8 -*-

valor= [4.0, 4.5, 5.0, 2.0, 1.5]
linha= input().split(' ')
cod,q= linha


total = valor[int(cod)-1]*int(q)
print('Total: R$ %.2f' %total)
