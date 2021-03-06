from __future__ import print_function
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from IntegralFlashData import IntegralFlashData

intdataname_co = 'co_ddt_time_est_E_internal_firsts_rhoddt-7.2.dat'
intdataname_cone = 'hybrid_ddt_time_est_E_internal_firsts.dat'

ifd = IntegralFlashData()
ifd.readInts(intdataname_co)
ifd.GramsToMsun()
co_data = ifd.getArrayData()
ifd.clrArrayData()
ifd.readInts(intdataname_cone)
ifd.GramsToMsun()
cone_data = ifd.getArrayData()
ifd.clrArrayData()

# Get averages and standard deviations for the plot
co_average_mass = np.average(co_data['mass with dens > 2e7'])
print('co ave mass: ' + str(co_average_mass))
co_std_mass = np.std(co_data['mass with dens > 2e7'])
print('co std mass: ' + str(co_std_mass))

print('\n---------------------------------\n')

cone_average_mass = np.average(cone_data['mass with dens > 2e7'])
print('cone ave mass: ' + str(cone_average_mass))
cone_std_mass = np.std(cone_data['mass with dens > 2e7'])
print('cone std mass: ' + str(cone_std_mass))

print('\n---------------------------------\n')

co_average_nse = np.average(co_data['final_nse_mass'])
print('co ave nse: ' + str(co_average_nse))
co_std_nse = np.std(co_data['final_nse_mass'])
print('co std nse: ' + str(co_std_nse))

print('\n---------------------------------\n')

cone_average_nse = np.average(cone_data['final_nse_mass'])
print('cone ave nse: ' + str(cone_average_nse))
cone_std_nse = np.std(cone_data['final_nse_mass'])
print('cone std nse: ' + str(cone_std_nse))

print('\n---------------------------------\n')

co_average_time = np.average(co_data['time'])
print('co ave time: ' + str(co_average_time))
co_std_time = np.std(co_data['time'])
print('co std time: ' + str(co_std_time))

print('\n---------------------------------\n')

cone_average_time = np.average(cone_data['time'])
print('cone ave time: ' + str(cone_average_time))
cone_std_time = np.std(cone_data['time'])
print('cone std time: ' + str(cone_std_time))

print('\n---------------------------------\n')

print('number of CO realizations: ' + str(len(co_data['final_nse_mass'])))
print('number of CONE realizations: ' + str(len(cone_data['final_nse_mass'])))

plt.figure(1)
fig = plt.gcf()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(co_data['mass with dens > 2e7'],co_data['final_nse_mass'],marker='o',markersize=5,linestyle='None',color='red')
ax1.plot(cone_data['mass with dens > 2e7'],cone_data['final_nse_mass'],marker='D',markersize=5,linestyle='None',color='green')
rect_co = plt.Rectangle((co_average_mass-co_std_mass,co_average_nse-co_std_nse),
                        2.0*co_std_mass,2.0*co_std_nse,facecolor='orange',
                        edgecolor='orange',alpha=0.7)
ax1.add_patch(rect_co)
rect_cone = plt.Rectangle((cone_average_mass-cone_std_mass,cone_average_nse-cone_std_nse),
                        2.0*cone_std_mass,2.0*cone_std_nse,facecolor='blue',
                        edgecolor='blue',alpha=0.7)
ax1.add_patch(rect_cone)

handles_cos = mlines.Line2D([],[],color='orange',alpha=0.7,
                            linestyle='-',linewidth=2.0,
                            label='CO Average ' + r'$\pm 1 \sigma$')
handles_com = mlines.Line2D([],[],color='red',marker='o',markersize=5,linestyle='None', label='CO Realizations')
handles_cones = mlines.Line2D([],[],color='blue',alpha=0.7,
                            linestyle='-',linewidth=2.0,
                            label='CONe Average '+r'$\pm 1 \sigma$')
handles_conem = mlines.Line2D([],[],color='green',marker='D',markersize=5,linestyle='None', label='CONe Realizations')

#plt.legend(handles=[mlco,mlco_fit,mlcone,mlcone_fit],loc=2,bbox_transform=plt.gcf().transFigure,prop={'size':16})
plt.legend(handles=[handles_com,handles_cos,handles_conem,handles_cones],loc=4,borderaxespad=0.0, borderpad=0.125, handletextpad=0.0,prop={'size':18})
plt.ylabel('Final IGE Yield ($\\mathrm{M_\\odot}$)')
plt.xlabel('Mass With Density $>2 \\times 10^7~ \\mathrm{g~{cm}^{-3}}$ at time of DDT ($\\mathrm{M_\\odot}$)')
#plt.title('Final IGE Yield vs.\ High Density Mass at DDT')

#plt.show()
plt.savefig('final_nse_mass_vs_high_density_mass_at_ddt.pdf',bbox_inches='tight',pad_inches=0.05)
