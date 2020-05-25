from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 9)
pdf.cell(100, 3, txt= "ООО БАНК \"Хоум-Кредит\"", align="L", border = "RLT", ln = 0)
pdf.cell(20, 3, txt= "БИК", align="L", border = 1, ln = 0)
pdf.cell(60, 3, txt= "40453535", align="L", border = "RLT", ln = 1)


pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 7)
pdf.cell(100, 3, txt= "", align="L", border = "RL", ln = 0)
pdf.set_font('DejaVu', '', 8)
pdf.cell(20, 3, txt= "Сч. №", align="L", border = "RLT", ln= 0)
pdf.cell(60, 3, txt= "8800553535", align="L", border = "RL", ln= 1)

pdf.set_font('DejaVu', '', 7)
pdf.cell(100, 7, txt= "Банк получателя", align="L", border = "RLB", ln = 0)
pdf.set_font('DejaVu', '', 8)
pdf.cell(20, 7, txt= "", align="L", border = "RLB", ln = 0)
pdf.cell(60, 7, txt= "", align="L", border = "RLB", ln = 1)

pdf.cell(10, 3, txt= "ИНН", align="L", border = "TLB", ln = 0)
pdf.cell(40, 3, txt= "223764784", align="L", border = "TRB", ln = 0)
pdf.cell(10, 3, txt= "КПП", align="L", border = "TLB", ln = 0)
pdf.cell(40, 3, txt= "9235255626", align="L", border = "TRB", ln = 0)
pdf.cell(20, 3, txt= "Сч. №", align="L", border = "RLT", ln= 0)
pdf.cell(60, 3, txt= "8800235235235", align="L", border = "RL", ln= 1)

pdf.cell(100, 7, txt= "ООО \"СОГАЗ И ВАЗ\"", align="L", border = "RLT", ln = 0)
pdf.cell(20, 7, txt= "", align="L", border = "RLT", ln= 0)
pdf.cell(60, 7, txt= "", align="L", border = "RL", ln= 1)

pdf.set_font('DejaVu', '', 7)
pdf.cell(100, 7, txt= "Получатель", align="L", border = "RLB", ln = 0)
pdf.cell(20, 7, txt= "", align="L", border = "RLB", ln = 0)
pdf.cell(60, 7, txt= "", align="L", border = "RLB", ln = 1)


pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
pdf.set_font('DejaVu', 'B', 12)
pdf.cell(100, 10, txt= "Счет на оплату № 52 от 28.03.2018 г.", align="L", border = 0, ln = 1)

pdf.set_line_width(0.5)
pdf.line(10, 55, 190, 55)
pdf.set_line_width(0.2)
pdf.ln(h = '')


pdf.set_font('DejaVu', '', 9)
pdf.cell(40, 3, txt= "Получатель", align="L", border = 0, ln = 0)
pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
pdf.set_font('DejaVu', 'B', 9)
pdf.cell(100, 3, txt= "ООО \"Фабрики рабочим\", г. Петроград, ул. Коммунистов 19к17", align="L", border = 0, ln = 1)

pdf.set_font('DejaVu', '', 9)
pdf.cell(20, 3, txt= "(Исполнитель):", align="L", border = 0, ln = 1)

pdf.ln(h = '')
pdf.set_font('DejaVu', '', 9)
pdf.cell(40, 3, txt= "Покупатель", align="L", border = 0, ln = 0)
pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
pdf.set_font('DejaVu', 'B', 9)
pdf.cell(100, 3, txt= "ООО \"Земля крестьянам\", г. Петроград, ул. Коммунистов 19к22", align="L", border = 0, ln = 1)

pdf.set_font('DejaVu', '', 9)
pdf.cell(20, 3, txt= "(Заказчик):", align="L", border = 0, ln = 1)

pdf.ln(h = '')
pdf.ln(h = '')
pdf.ln(h = '')

pdf.set_font('DejaVu', '', 7)
pdf.cell(40, 3, txt= "Основание:", align="L", border = 0, ln = 0)

pdf.set_font('DejaVu', 'B', 7)
pdf.cell(40, 3, txt= "№ 874004961 от 18.03.2018", align="L", border = 0, ln = 1)

pdf.set_font('DejaVu', 'B', 8)
pdf.cell(5, 10, txt= "№", align="C", border = "RLTB", ln = 0)
pdf.cell(115, 10, txt= "Товары(работы. услуги)", align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= "Кол-во", align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= "Цена", align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= "Сумма", align="C", border = "RLTB", ln = 1)

in_call_minutes = '17.45'
out_call_minutes = '83.22'
sms_amount = '73'
internet_trf_Kb = '180.39'

in_call_price = '0 руб/мин'
out_call_price = '2 руб/мин'
sms_price = '1 руб/смс'
internet_price = '1 руб/КБ'

in_call_sum = float(in_call_minutes) * 0
out_call_sum = float(out_call_minutes) * 2
sms_sum = float(sms_amount) * 1 - 10
internet_sum = (float(internet_trf_Kb) - 200) + 200 * 0.5
result = in_call_sum + out_call_sum + sms_sum + internet_sum
nds = result * 20 / 100

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

in_call_sum = toFixed(in_call_sum, 2)
out_call_sum = toFixed(out_call_sum, 2)
sms_sum = toFixed(sms_sum, 2)
internet_sum = toFixed(internet_sum, 2)
result = toFixed(result, 2)
nds = toFixed(nds, 2)

pdf.set_font('DejaVu', '', 8)
pdf.cell(5, 10, txt= "1", align="C", border = "RLTB", ln = 0)
pdf.cell(115, 10, txt= "Исходящие вызовы", align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= out_call_minutes, align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= out_call_price, align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= out_call_sum, align="C", border = "RLTB", ln = 1)

pdf.cell(5, 10, txt= "2", align="C", border = "RLTB", ln = 0)
pdf.cell(115, 10, txt= "Входящие вызовы", align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= in_call_minutes, align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= in_call_price, align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= in_call_sum, align="C", border = "RLTB", ln = 1)

pdf.cell(5, 10, txt= "3", align="C", border = "RLTB", ln = 0)
pdf.cell(115, 10, txt= "СМС", align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= sms_amount, align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= sms_price + '*', align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= sms_sum, align="C", border = "RLTB", ln = 1)

pdf.cell(5, 10, txt= "4", align="C", border = "RLTB", ln = 0)
pdf.cell(115, 10, txt= "Интернет трафик", align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= internet_trf_Kb, align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= internet_price + '**', align="C", border = "RLTB", ln = 0)
pdf.cell(20, 10, txt= internet_sum, align="C", border = "RLTB", ln = 1)

pdf.set_font('DejaVu', '', 7)
pdf.cell(100, 3, txt= '*Тарифный план "СМС" включает в себя 10 бесплатных СМС', align="L", border = 0, ln = 1)
pdf.cell(100, 3, txt= '**В тарифный план "Интернет" включены первые 200 КБ по цене 0.5 руб/КБ', align="L", border = 0, ln = 1)

pdf.cell(140)
pdf.set_font('DejaVu', 'B', 7)
pdf.cell(20, 5, txt= 'Итого:', align="R", border = 0, ln = 0)
pdf.cell(20, 5, txt= result + ' руб', align="C", border = 0, ln = 1)
pdf.cell(140)
pdf.cell(20, 5, txt= 'В том числе НДС:', align="R", border = 0, ln = 0)
pdf.cell(20, 5, txt= nds + ' руб', align="C", border = 0, ln = 1)
pdf.cell(140)
pdf.cell(20, 5, txt= 'Всего к оплате:', align="R", border = 0, ln = 0)
pdf.cell(20, 5, txt= result + ' руб', align="C", border = 0, ln = 1)

pdf.set_font('DejaVu', '', 8)
pdf.cell(140, 5, txt= 'Всего 4 наименования на сумму ' +  result + ' руб.', align="L", border = 0, ln = 1)
pdf.set_font('DejaVu', 'B', 8)
pdf.cell(140, 5, txt= 'Триста девять рублей 83 копейки', align="L", border = 0, ln = 1)

pdf.ln(h = '')
pdf.ln(h = '')
pdf.ln(h = '')
pdf.set_font('DejaVu', '', 7)
pdf.cell(140, 4, txt= 'Внимание!', align="L", border = 0, ln = 1)
pdf.cell(140, 4, txt= 'Оплата данного счета означает согласие с условиями поставки товара.', align="L", border = 0, ln = 1)
pdf.cell(140, 4, txt= 'Уведомление об оплате обязательно, в противном случае не гарантируется наличие товара на складе.', align="L", border = 0, ln = 1)
pdf.cell(140, 4, txt= 'Товар отпускается по факту прихода денег на р/с Поставщика, самовывозом, при наличии доверенности и паспорта.', align="L", border = 0, ln = 1)



pdf.set_line_width(0.5)
pdf.line(10, 205, 190, 205)
pdf.set_line_width(0.1)

pdf.ln(h = '')
pdf.ln(h = '')
pdf.ln(h = '')
pdf.ln(h = '')
pdf.set_font('DejaVu', 'B', 8)
pdf.cell(25, 5, txt= 'Руководитель', align="L", border = 0, ln = 0)
pdf.set_font('DejaVu', '', 8)
pdf.cell(50, 5, txt= 'Низачторасстрелов М.В.', align="C", border = "B", ln = 0)

pdf.cell(30)

pdf.set_font('DejaVu', 'B', 8)
pdf.cell(25, 5, txt= 'Бухгалтер', align="L", border = 0, ln = 0)
pdf.set_font('DejaVu', '', 8)
pdf.cell(50, 5, txt= 'Сергеев А.С.', align="C", border = "B", ln = 0)

pdf.output("bill.pdf")