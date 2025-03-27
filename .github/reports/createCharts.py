import json
import matplotlib
matplotlib.use('Agg')  # Usa il backend 'Agg' che non richiede GUI
import matplotlib.pyplot as plt

# Carica il JSON
with open('report.json', 'r') as f:
    data = json.load(f)

# Estrai metriche per classe
class_names = []
fan_in_values = []
fan_out_values = []
attributes = []
method_names = []
method_parameters = []
method_lines = []

for class_name, class_data in data['class_metrics'].items():
    class_names.append(class_name)
    fan_in_values.append(class_data['fan_in'])
    fan_out_values.append(class_data['fan_out'])
    attributes.append(class_data['attributes'])

    for method_name, method_data in class_data['methods'].items():
        method_names.append(class_name+"."+method_name)
        method_parameters.append(method_data['parameters'])
        method_lines.append(method_data['lines'])


# 1. Numero di metodi per classe
plt.figure(figsize=(10, 12))
plt.barh(class_names, attributes)
plt.xlabel("Numero di attributi")
plt.ylabel("Classi")
plt.title("Attrbuti per classe")
plt.margins(y=0.03)
plt.tight_layout()
plt.savefig(f'metrics_attributes.png')
plt.close()

# # 2. Fan-in per classe
plt.figure(figsize=(10, 12))
plt.barh(class_names, fan_in_values)
plt.xlabel("Fan-IN")
plt.ylabel("Classi")
plt.title("Fan-IN per classe")
plt.margins(y=0.03)
plt.tight_layout()
plt.savefig(f'metrics_fan_in.png')
plt.close()

# # 3. Linee totali di codice per classe
plt.figure(figsize=(10, 12))
plt.barh(class_names, fan_out_values)
plt.xlabel("Fan-OUT")
plt.ylabel("Classi")
plt.title("Fan-OUT per classe")
plt.margins(y=0.03)
plt.tight_layout()
plt.savefig(f'metrics_fan_out.png')
plt.close()

# # 4. Parametri totali per metodo
plt.figure(figsize=(10, 20))
plt.barh(method_names, method_parameters)
plt.xlabel("Numero di parametri") 
plt.ylabel("Metodi")
plt.title("Parametri per metodo")
plt.margins(y=0.03)
plt.tight_layout()
plt.savefig(f'metrics_parameters.png')
plt.close()

# # 4. Linee totali per metodo
plt.figure(figsize=(10, 20))
plt.barh(method_names, method_lines)
plt.xlabel("Numero di linee")
plt.ylabel("Metodi")
plt.title("Linee per metodo")
plt.margins(y=0.03)
plt.tight_layout()
plt.savefig(f'metrics_lines.png')
plt.close()