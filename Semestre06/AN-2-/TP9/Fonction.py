import math

# ===================
#  Exemple Du Cours
# ===================
f      = lambda x, y: -y + x + 1
dfdx   = lambda x, y: 1
dfdy   = lambda x, y: -1
y_exact = lambda x: math.exp(-x) + x


# ===================
#  Affichage Soigné
# ===================
def afficher_tableau(table):
    label = ["x_K", "y(x_K)", "y_K", "y(x_K)-y_K"]    
    def inf_value(x):
        if abs(x) < 0.0001 and x != 0:
            exp = math.floor(math.log10(abs(x)))
            factor = x / (10 ** exp)
            return f"{factor:.3f} * 10^{exp}"
        return f"{x:.4f}"

    rows_data = []
    col_widths = [len(l) for l in label]      
    for row in table:
        x_val, yx_val, y_val = row
        diff = abs(yx_val - y_val)
        formatted = [
            f"{x_val:.1f}",
            inf_value(yx_val),
            inf_value(y_val),
            inf_value(diff)
        ]
        rows_data.append(formatted)
        for i, s in enumerate(formatted):
            col_widths[i] = max(col_widths[i], len(s))    
    col_widths = [w + 2 for w in col_widths]
    
    def draw_separator():
        line = '+' + '+'.join('-' * w for w in col_widths) + '+'
        print(line)
    
    draw_separator()
    header_line = '|' + '|'.join(f" {label[i]:<{col_widths[i]-2}} " for i in range(4)) + '|'
    print(header_line)
    draw_separator()
    for row in rows_data:
        data_line = '|' + '|'.join(f" {row[i]:<{col_widths[i]-2}} " for i in range(4)) + '|'
        print(data_line)
        draw_separator()