import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Datos de ejemplo inspirados en Oracle (en millones de USD, aproximados y simplificados)
def balance_sheet_data():
    # Activos (Assets)
    cash = 21500  # Efectivo y equivalentes
    accounts_receivable = 5600  # Cuentas por cobrar
    inventory = 300  # Inventario (bajo, típico de empresas de software)
    current_assets = cash + accounts_receivable + inventory
    property_plant_equipment = 7200  # Propiedad, planta y equipo
    intangible_assets = 43000  # Activos intangibles (patentes, licencias, etc.)
    goodwill = 45000  # Goodwill (valor de adquisiciones)
    non_current_assets = property_plant_equipment + intangible_assets + goodwill
    total_assets = current_assets + non_current_assets

    # Pasivos (Liabilities)
    accounts_payable = 800  # Cuentas por pagar
    short_term_debt = 3500  # Deuda a corto plazo
    deferred_revenue = 8500  # Ingresos diferidos (típico en software)
    current_liabilities = accounts_payable + short_term_debt + deferred_revenue
    long_term_debt = 75000  # Deuda a largo plazo
    non_current_liabilities = long_term_debt
    total_liabilities = current_liabilities + non_current_liabilities

    # Patrimonio (Equity)
    common_stock = 31000  # Acciones comunes
    retained_earnings = 2500  # Ganancias retenidas (puede ser bajo por dividendos o recompras)
    total_equity = common_stock + retained_earnings

    total_liabilities_and_equity = total_liabilities + total_equity

    return {
        'assets': {
            'Cash and Equivalents': cash,
            'Accounts Receivable': accounts_receivable,
            'Inventory': inventory,
            'Current Assets': current_assets,
            'Property, Plant, Equipment': property_plant_equipment,
            'Intangible Assets': intangible_assets,
            'Goodwill': goodwill,
            'Non-Current Assets': non_current_assets,
            'Total Assets': total_assets
        },
        'liabilities': {
            'Accounts Payable': accounts_payable,
            'Short-Term Debt': short_term_debt,
            'Deferred Revenue': deferred_revenue,
            'Current Liabilities': current_liabilities,
            'Long-Term Debt': long_term_debt,
            'Non-Current Liabilities': non_current_liabilities,
            'Total Liabilities': total_liabilities
        },
        'equity': {
            'Common Stock': common_stock,
            'Retained Earnings': retained_earnings,
            'Total Equity': total_equity,
            'Total Liabilities and Equity': total_liabilities_and_equity
        }
    }

def income_statement_data():
    # Estado de Resultados (en millones de USD, año fiscal aproximado)
    revenue = 50000  # Ingresos (ventas de software, cloud, licencias)
    cost_of_goods_sold = 14000  # Costo de ventas (costos de cloud, soporte)
    gross_profit = revenue - cost_of_goods_sold
    operating_expenses = 21000  # Gastos operativos (R&D, ventas, administrativos)
    operating_income = gross_profit - operating_expenses
    interest_expense = 2500  # Gastos por intereses (deuda)
    other_income = 500  # Otros ingresos (inversiones, etc.)
    income_before_taxes = operating_income - interest_expense + other_income
    income_tax = 2000  # Impuestos
    net_income = income_before_taxes - income_tax

    return {
        'Revenue': revenue,
        'Cost of Goods Sold': cost_of_goods_sold,
        'Gross Profit': gross_profit,
        'Operating Expenses': operating_expenses,
        'Operating Income': operating_income,
        'Interest Expense': interest_expense,
        'Other Income': other_income,
        'Income Before Taxes': income_before_taxes,
        'Income Tax': income_tax,
        'Net Income': net_income
    }

def cash_flow_statement_data():
    # Flujo de Efectivo (en millones de USD, año fiscal aproximado)
    net_income = income_statement_data()['Net Income']
    depreciation_amortization = 3000  # Depreciación y amortización
    changes_in_working_capital = -500  # Cambios en capital de trabajo
    cash_from_operations = net_income + depreciation_amortization + changes_in_working_capital
    capital_expenditures = -2000  # Gastos de capital (compra de equipo)
    acquisitions = -1500  # Adquisiciones
    cash_from_investing = capital_expenditures + acquisitions
    debt_issuance = 5000  # Emisión de deuda
    dividends_paid = -4000  # Dividendos pagados
    stock_repurchasing = -10000  # Recompra de acciones
    cash_from_financing = debt_issuance + dividends_paid + stock_repurchasing
    net_change_in_cash = cash_from_operations + cash_from_investing + cash_from_financing

    return {
        'operating': {
            'Net Income': net_income,
            'Depreciation and Amortization': depreciation_amortization,
            'Changes in Working Capital': changes_in_working_capital,
            'Cash from Operating Activities': cash_from_operations
        },
        'investing': {
            'Capital Expenditures': capital_expenditures,
            'Acquisitions': acquisitions,
            'Cash from Investing Activities': cash_from_investing
        },
        'financing': {
            'Debt Issuance': debt_issuance,
            'Dividends Paid': dividends_paid,
            'Stock Repurchasing': stock_repurchasing,
            'Cash from Financing Activities': cash_from_financing
        },
        'net_change': {
            'Net Change in Cash': net_change_in_cash
        }
    }

# Mostrar sección genérica
def display_section(frame, title, items, total_label=None, bold_items=None):
    ttk.Label(frame, text=title, font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 0))
    ttk.Label(frame, text="----------------").pack(anchor="w")
    for key, value in items.items():
        if bold_items and key not in bold_items:
            continue
        font_style = ("Arial", 10, "bold") if bold_items and key in bold_items else ("Arial", 10)
        ttk.Label(frame, text=f"  {key}: ${value:,.2f}M", font=font_style).pack(anchor="w")
    if total_label:
        ttk.Label(frame, text=total_label, font=("Arial", 10, "bold")).pack(anchor="w", pady=(5, 10))

# Gráfico para Balance Sheet
def create_balance_chart(data):
    fig, ax = plt.subplots(figsize=(6, 4))
    categories = ['Current Assets', 'Non-Current Assets', 'Current Liabilities', 'Non-Current Liabilities', 'Equity']
    values = [
        data['assets']['Current Assets'],
        data['assets']['Non-Current Assets'],
        data['liabilities']['Current Liabilities'],
        data['liabilities']['Non-Current Liabilities'],
        data['equity']['Total Equity']
    ]
    colors = ['#66b3ff', '#99ccff', '#ff9999', '#ff6666', '#99ff99']
    ax.bar(categories, values, color=colors)
    ax.set_title("Balance Sheet Breakdown", fontsize=14)
    ax.set_ylabel("Amount ($M)", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    for i, v in enumerate(values):
        ax.text(i, v + 1000, f"${v:,.2f}M", ha='center', fontsize=9)
    plt.tight_layout()
    return fig

# Gráfico para Income Statement
def create_income_chart(data):
    fig, ax = plt.subplots(figsize=(6, 4))
    categories = ['Revenue', 'Gross Profit', 'Operating Income', 'Net Income']
    values = [data['Revenue'], data['Gross Profit'], data['Operating Income'], data['Net Income']]
    colors = ['#66b3ff', '#99ccff', '#66cc66', '#33cc33']
    ax.bar(categories, values, color=colors)
    ax.set_title("Income Statement Breakdown", fontsize=14)
    ax.set_ylabel("Amount ($M)", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    for i, v in enumerate(values):
        ax.text(i, v + 1000, f"${v:,.2f}M", ha='center', fontsize=9)
    plt.tight_layout()
    return fig

# Gráfico para Cash Flow Statement
def create_cash_flow_chart(data):
    fig, ax = plt.subplots(figsize=(6, 4))
    categories = ['Operating Cash', 'Investing Cash', 'Financing Cash', 'Net Change in Cash']
    values = [
        data['operating']['Cash from Operating Activities'],
        data['investing']['Cash from Investing Activities'],
        data['financing']['Cash from Financing Activities'],
        data['net_change']['Net Change in Cash']
    ]
    colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffd700']
    ax.bar(categories, values, color=colors)
    ax.set_title("Cash Flow Breakdown", fontsize=14)
    ax.set_ylabel("Amount ($M)", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    for i, v in enumerate(values):
        ax.text(i, v + 1000 if v > 0 else v - 2000, f"${v:,.2f}M", ha='center', fontsize=9)
    plt.tight_layout()
    return fig

# Crear la interfaz gráfica
def create_gui():
    # Obtener datos
    bs_data = balance_sheet_data()
    is_data = income_statement_data()
    cf_data = cash_flow_statement_data()

    # Ventana principal
    root = tk.Tk()
    root.title("Oracle-Style Financial Statements")
    root.geometry("1000x600")

    # Manejador para cerrar
    def on_closing():
        plt.close('all')
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Notebook para pestañas
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Frame para Balance Sheet
    bs_frame = ttk.Frame(notebook)
    notebook.add(bs_frame, text="Balance Sheet")

    # Frame para datos numéricos del Balance Sheet
    bs_text_frame = ttk.Frame(bs_frame, padding="15")
    bs_text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    ttk.Label(bs_text_frame, text="BALANCE SHEET (BALANCE GENERAL)", font=("Arial", 16, "bold")).pack(pady=10)
    display_section(bs_text_frame, "ACTIVOS (Assets)", bs_data['assets'],
                    total_label=f"TOTAL ACTIVOS: ${bs_data['assets']['Total Assets']:,.2f}M",
                    bold_items=['Cash and Equivalents', 'Accounts Receivable', 'Inventory',
                                'Property, Plant, Equipment', 'Intangible Assets', 'Goodwill'])
    display_section(bs_text_frame, "PASIVOS (Liabilities)", bs_data['liabilities'],
                    total_label=f"TOTAL PASIVOS: ${bs_data['liabilities']['Total Liabilities']:,.2f}M",
                    bold_items=['Accounts Payable', 'Short-Term Debt', 'Deferred Revenue', 'Long-Term Debt'])
    display_section(bs_text_frame, "PATRIMONIO (Equity)", bs_data['equity'],
                    total_label=f"TOTAL PATRIMONIO: ${bs_data['equity']['Total Equity']:,.2f}M",
                    bold_items=['Common Stock', 'Retained Earnings'])
    ttk.Label(bs_text_frame, text=f"TOTAL PASIVOS Y PATRIMONIO: ${bs_data['equity']['Total Liabilities and Equity']:,.2f}M",
              font=("Arial", 10, "bold")).pack(anchor="w", pady=(5, 10))
    verification_text = ("Verificación: Activos = Pasivos + Patrimonio (Balanceado)"
                         if bs_data['assets']['Total Assets'] == bs_data['equity']['Total Liabilities and Equity']
                         else "Error: Los totales no coinciden!")
    verification_color = "green" if "Balanceado" in verification_text else "red"
    ttk.Label(bs_text_frame, text=verification_text, font=("Arial", 10, "italic"),
              foreground=verification_color).pack(anchor="w")

    # Gráfico para Balance Sheet
    bs_fig = create_balance_chart(bs_data)
    bs_canvas = FigureCanvasTkAgg(bs_fig, master=bs_frame)
    bs_canvas.draw()
    bs_canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Frame para Income Statement
    is_frame = ttk.Frame(notebook)
    notebook.add(is_frame, text="Income Statement")

    # Frame para datos numéricos del Income Statement
    is_text_frame = ttk.Frame(is_frame, padding="15")
    is_text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    ttk.Label(is_text_frame, text="INCOME STATEMENT\n(ESTADO DE RESULTADOS)", font=("Arial", 16, "bold")).pack(pady=10)
    display_section(is_text_frame, "RESULTADOS", is_data,
                    total_label=f"NET INCOME: ${is_data['Net Income']:,.2f}M",
                    bold_items=['Revenue', 'Cost of Goods Sold', 'Gross Profit', 'Operating Expenses',
                                'Operating Income', 'Interest Expense', 'Other Income', 'Income Before Taxes', 'Income Tax'])

    # Gráfico para Income Statement
    is_fig = create_income_chart(is_data)
    is_canvas = FigureCanvasTkAgg(is_fig, master=is_frame)
    is_canvas.draw()
    is_canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Frame para Cash Flow Statement
    cf_frame = ttk.Frame(notebook)
    notebook.add(cf_frame, text="Cash Flow Statement")

    # Frame con scroll para datos numéricos del Cash Flow Statement
    cf_canvas = tk.Canvas(cf_frame)
    cf_scrollbar = ttk.Scrollbar(cf_frame, orient="vertical", command=cf_canvas.yview)
    cf_text_frame = ttk.Frame(cf_canvas)
    cf_canvas.configure(yscrollcommand=cf_scrollbar.set)
    cf_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    cf_scrollbar.pack(side=tk.LEFT, fill=tk.Y)
    cf_canvas.create_window((0, 0), window=cf_text_frame, anchor="nw")
    
    # Actualizar el área de desplazamiento
    def configure_scroll(event):
        cf_canvas.configure(scrollregion=cf_canvas.bbox("all"))
    cf_text_frame.bind("<Configure>", configure_scroll)

    ttk.Label(cf_text_frame, text="CASH FLOW STATEMENT\n(ESTADO DE FLUJOS DE EFECTIVO)", font=("Arial", 16, "bold")).pack(pady=10)
    display_section(cf_text_frame, "OPERATING ACTIVITIES", cf_data['operating'],
                    total_label=f"CASH FROM OPERATING ACTIVITIES: ${cf_data['operating']['Cash from Operating Activities']:,.2f}M",
                    bold_items=['Net Income', 'Depreciation and Amortization', 'Changes in Working Capital'])
    display_section(cf_text_frame, "INVESTING ACTIVITIES", cf_data['investing'],
                    total_label=f"CASH FROM INVESTING ACTIVITIES: ${cf_data['investing']['Cash from Investing Activities']:,.2f}M",
                    bold_items=['Capital Expenditures', 'Acquisitions'])
    display_section(cf_text_frame, "FINANCING ACTIVITIES", cf_data['financing'],
                    total_label=f"CASH FROM FINANCING ACTIVITIES: ${cf_data['financing']['Cash from Financing Activities']:,.2f}M",
                    bold_items=['Debt Issuance', 'Dividends Paid', 'Stock Repurchasing'])
    display_section(cf_text_frame, "NET CHANGE", cf_data['net_change'],
                    total_label=f"NET CHANGE IN CASH: ${cf_data['net_change']['Net Change in Cash']:,.2f}M",
                    bold_items=['Net Change in Cash'])

    # Gráfico para Cash Flow Statement
    cf_fig = create_cash_flow_chart(cf_data)
    cf_canvas_fig = FigureCanvasTkAgg(cf_fig, master=cf_frame)
    cf_canvas_fig.draw()
    cf_canvas_fig.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Ejecutar la ventana
    root.mainloop()

# Ejecutar la interfaz
if __name__ == "__main__":
    create_gui()