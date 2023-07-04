from assets.libraries import *

LOGO_LAB='./static/logolab.png'
LOGO_IIP='./static/logoiip.png'
PREGUNTAS_TODAS=    ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39']
PREGUNTAS_BINARIAS= ['p1','p2','p13','p14','p15','p16',            'p19','p20',            'p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39']
PREGUNTAS_BUCLES=   ['p1','p2','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24_1','p24_2','p24_3','p24_4','p24_5','p25','p26','p27','p28',            'p31','p32','p33','p34','p35','p36','p37','p38','p39']
ENTIDAD_INICIAL='Instituto De Desarrollo Urbano'
PREGUNTA_INICIAL='p2'

preguntas_df=pd.read_excel('./files/preguntas/leyenda_columnas.xlsx')

respuestas_2021_df=pd.read_excel('./files/respuestas/2021/respuestas_2021.xlsx')
respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

entidades_2023=list(respuestas_2023_df['entidad'].sort_values())

resultados_2021_df=pd.read_excel('./files/resultados/2021/resultados_2021.xlsx')
resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')

p1_df=pd.read_excel('./files/separadas/repeat_p1.xlsx')
p2_df=pd.read_excel('./files/separadas/repeat_p2.xlsx')
p13_df=pd.read_excel('./files/separadas/repeat_p13.xlsx')
p14_df=pd.read_excel('./files/separadas/repeat_p14.xlsx')
p15_df=pd.read_excel('./files/separadas/repeat_p15.xlsx')
p16_df=pd.read_excel('./files/separadas/repeat_p16.xlsx')
p17_df=pd.read_excel('./files/separadas/repeat_p17.xlsx')
p18_df=pd.read_excel('./files/separadas/repeat_p18.xlsx')
p19_df=pd.read_excel('./files/separadas/repeat_p19.xlsx')
p20_df=pd.read_excel('./files/separadas/repeat_p20.xlsx')
p21_df=pd.read_excel('./files/separadas/repeat_p21.xlsx')
p22_df=pd.read_excel('./files/separadas/repeat_p22.xlsx')
p23_df=pd.read_excel('./files/separadas/repeat_p23.xlsx')
p24_1_df=pd.read_excel('./files/separadas/repeat_p24_1.xlsx')
p24_2_df=pd.read_excel('./files/separadas/repeat_p24_2.xlsx')
p24_3_df=pd.read_excel('./files/separadas/repeat_p24_3.xlsx')
p24_4_df=pd.read_excel('./files/separadas/repeat_p24_4.xlsx')
p24_5_df=pd.read_excel('./files/separadas/repeat_p24_5.xlsx')
p25_df=pd.read_excel('./files/separadas/repeat_p25.xlsx')
p26_df=pd.read_excel('./files/separadas/repeat_p26.xlsx')
p27_df=pd.read_excel('./files/separadas/repeat_p27.xlsx')
p28_df=pd.read_excel('./files/separadas/repeat_p28.xlsx')
p31_df=pd.read_excel('./files/separadas/repeat_p31.xlsx')
p32_df=pd.read_excel('./files/separadas/repeat_p32.xlsx')
p33_df=pd.read_excel('./files/separadas/repeat_p33.xlsx')
p34_df=pd.read_excel('./files/separadas/repeat_p34.xlsx')
p35_df=pd.read_excel('./files/separadas/repeat_p35.xlsx')
p36_df=pd.read_excel('./files/separadas/repeat_p36.xlsx')
p37_df=pd.read_excel('./files/separadas/repeat_p37.xlsx')
p38_df=pd.read_excel('./files/separadas/repeat_p38.xlsx')
p39_df=pd.read_excel('./files/separadas/repeat_p39.xlsx')


CRITS_PREGUNTAS_BASE={
    'p1':{},
    'p2':{'c1':0,'c2':0,'c3':['c1','c2','c3','m_i']},
    'p3':{'c1':1,},
    'p4':{'c1':0,'c2':0},
    'p5':{'c1':1},
    'p6':{'c1':0,'c2':0},
    'p7':{'c1':1},
    'p8':{'c1':0,'c2':0},
    'p9':{},
    'p10':{'c1':1},
    'p11':{'c1':0,'c2':0},
    'p12':{},
    'p13':{'c1':0,'c2':['c1','c2','c3','m_i']},
    'p14':{'c1':['c1','c2','c3','s_i'],'c2':0},
    'p15':{'c1':['c1','c2','c3','s_i'],'c2':0},
    'p16':{'c1':['c1','c2','c3','s_i'],'c2':0},
    'p17':{'c1':['c1','c2','c3','s_i'],'c2':0},
    'p18':{'c1':['c1','c2','c3','s_i'],'c2':0},
    'p19':{'c1':['c1','c2','c3','s_i'],'c2':0},
    'p20':{'c1':['c1','c2','c3','s_i'],'c2':0},
    'p21':{'c1':['c1','c2','c3','s_i'],'c2':0},
    'p22':{'c1':['c1','c2','c3','s_i'],'c2':0},
    'p23':{'c1':['c1','c2','c3','c4','s_i','c5','c6']},
    'p24':{'c1':0},
    'p24_1':{'c1':0},
    'p24_2':{'c1':0},
    'p24_3':{'c1':0},
    'p24_4':{'c1':0},
    'p24_5':{'c1':0},
    'p25':{'c1':['c1','c2','c3','s_i'],'c2':['c4']},
    'p26':{'c1':['c1','c2','c3','s_i'],'c2':['c4']},
    'p27':{'c1':['c1']},
    'p28':{'c1':['c1','c2','c3','c4','c5','c6','s_i','c7']},
    'p29':{'c1':0},
    'p30':{'c1':0},
    'p31':{'c1':0,'c2':0},
    'p32':{'c1':0,'c2':0},
    'p33':{'c1':0,'c2':0},
    'p34':{'c1':0,'c2':0},
    'p35':{'c1':0,'c2':0},
    'p36':{'c1':0,'c2':0},
    'p37':{'c1':0,'c2':0},
    'p38':{'c1':0,'c2':0},
    'p39':{'c1':0,'c2':0},
    }

"""
CRITS_PREGUNTAS_BASE={
    'p1':{},
    'p2':{'cri_p2_c1':0,'cri_p2_c2':0,'cri_p2_c3':['c1','c2','c3','m_i']},
    'p3':{'cri_p3_c1':1,},
    'p4':{'cri_p4_c1':0,'cri_p4_c2':0},
    'p5':{'cri_p5_c1':1},
    'p6':{'cri_p6_c1':0,'cri_p6_c2':0},
    'p7':{'cri_p7_c1':1},
    'p8':{'cri_p8_c1':0,'cri_p8_c2':0},
    'p9':{},
    'p10':{'cri_p10_c1':1},
    'p11':{'cri_p11_c1':0,'cri_p11_c2':0},
    'p12':{},
    'p13':{'cri_p13_c1':0,'cri_p13_c2':['c1','c2','c3','m_i']},
    'p14':{'cri_p14_c1':['c1','c2','c3','s_i'],'cri_p14_c2':['c4']},
    'p15':{'cri_p15_c1':['c1','c2','c3','s_i'],'cri_p15_c2':['c4']},
    'p16':{'cri_p16_c1':['c1','c2','c3','s_i'],'cri_p16_c2':['c4']},
    'p17':{'cri_p17_c1':['c1','c2','c3','s_i'],'cri_p17_c2':['c4']},
    'p18':{'cri_p18_c1':['c1','c2','c3','s_i'],'cri_p18_c2':['c4']},
    'p19':{'cri_p19_c1':['c1','c2','c3','s_i'],'cri_p19_c2':['c4']},
    'p20':{'cri_p20_c1':['c1','c2','c3','s_i'],'cri_p20_c2':['c4']},
    'p21':{'cri_p21_c1':['c1','c2','c3','s_i'],'cri_p21_c2':['c4']},
    'p22':{'cri_p22_c1':['c1','c2','c3','s_i'],'cri_p22_c2':['c4']},
    'p23':{'cri_p23_c1':['c1','c2','c3','c4','s_i','c5','c6']},
    'p24':{'cri_p24_c1':0},
    'p24_1':{'cri_p2_c1':0},
    'p24_2':{'cri_p2_c1':0},
    'p24_3':{'cri_p2_c1':0},
    'p24_4':{'cri_p2_c1':0},
    'p24_5':{'cri_p2_c1':0},
    'p25':{'cri_p25_c1':['c1','c2','c3','s_i'],'cri_p25_c2':['c4']},
    'p26':{'cri_p26_c1':['c1','c2','c3','s_i'],'cri_p26_c2':['c4']},
    'p27':{'cri_p27_c1':['c1']},
    'p28':{'cri_p28_c1':['c1','c2','c3','c4','c5','c6','s_i','c7']},
    'p29':{'cri_p29_c1':0},
    'p30':{'cri_p30_c1':0},
    'p31':{'cri_p31_c1':0,'cri_p31_c2':0},
    'p32':{'cri_p32_c1':0,'cri_p32_c2':0},
    'p33':{'cri_p33_c1':0,'cri_p33_c2':0},
    'p34':{'cri_p34_c1':0,'cri_p34_c2':0},
    'p35':{'cri_p35_c1':0,'cri_p35_c2':0},
    'p36':{'cri_p36_c1':0,'cri_p36_c2':0},
    'p37':{'cri_p37_c1':0,'cri_p37_c2':0},
    'p38':{'cri_p38_c1':0,'cri_p38_c2':0},
    'p39':{'cri_p39_c1':0,'cri_p39_c2':0},
    }
"""