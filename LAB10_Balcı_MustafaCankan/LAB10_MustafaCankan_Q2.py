import numpy as np
import matplotlib.pyplot as plt


student = np.loadtxt('students.txt',skiprows=1)
half = np.where(student[:,0] == 2)
half = student[half]

plt.figure(1)
plt.subplot(2,2,1)
plt.hist(half[:,3],4)
plt.title('Frequency of Math Grade of Half Sc. Students')

plt.subplot(2,2,3)
labels = 'Full','Half','Non'
full = np.where(student[:,0] == 1)
non = np.where(student[:,0] == 3)
list_labels = [ len(full[0]), len(half), len(non[0])]
explode = [0.0,0.0,0.1]
plt.pie(list_labels, labels=labels,explode= explode, autopct='%1.1f%%')
plt.title('Scholarship Percentages')

plt.subplot(2,2,2)
number_student_half = np.arange(1,len(half)+1,1)
plt.plot(number_student_half,half[:,1], "mo--", number_student_half,half[:,2], 'cx-')
plt.ylabel('Grades')
plt.legend(['Math','Reading'])
plt.title('Math vs Reading of Half Sc. Students')

plt.subplot(2,2,4)
mean_half = half[:,3].mean()
mean_student = student[:,3].mean()
mean_list = [mean_half,mean_student]
plt.bar('Half Sc.',mean_half)
plt.bar('All.',mean_student)
plt.ylabel('Average of Grades')
plt.title('Frequency of Math Grade of Half Sc. Students')
plt.show()
