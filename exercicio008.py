# Escreva um programa que leia um valor em metros e o exiba convertido em quilômetros, hectômetros, decâmetros, metros, centímetros e milímetros

medida = float(input('Digite um valor em metros: '))
mm = medida * 1000 # milímetro 
cm = medida * 100 # centímetro
dm = medida * 10 # decímetro
m = medida * 1 # metro
dam = medida / 10 # decâmetro
hm = medida / 100 # hectômetro
km = medida / 1000 # quilômetro

print(f'''O valor de {medida} 
Em quilômetros é {km:.4f}
Em hectômetro é {hm:.3f}
Em decâmetro é {dam:.2f}
Em metros é {m}
Em decímetro é {dm:.0f}
Em centímetros é {cm:.0f} 
Em milímetros é {mm:.0f}''')


