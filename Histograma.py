from mtbpy import mtbpy
import matplotlib.pyplot as plt
import sys

dadosc1 = mtbpy.mtb_instance().get_column(sys.argv[1:][0])
dadosc2 = mtbpy.mtb_instance().get_column(sys.argv[1:][1])

dados = [dadosc1, dadosc2]

fig, ax = plt.subplots()
ax.set_title('Histograma')
ax.hist(dados, histtype='barstacked')

fig.savefig("histograma.png") 
mtbpy.mtb_instance().add_image("histograma.png")
