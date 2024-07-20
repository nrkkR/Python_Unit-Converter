import tkinter as tk
from tkinter import ttk

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter App")

        # Create a tab control to organize different categories of converters
        self.tab_control = ttk.Notebook(root)
        self.tab_control.pack(expand=1, fill="both")

        # Add multiple converter categories
        self.length_converter()
        self.weight_converter()
        self.temperature_converter()
        self.volume_converter()

    def length_converter(self):
        frame = ttk.Frame(self.tab_control)
        frame.pack(fill="both", expand=1)

        # Labels and entry fields
        label = ttk.Label(frame, text="Enter Length:")
        label.grid(row=0, column=0, padx=10, pady=10)
        entry = ttk.Entry(frame, width=20)
        entry.grid(row=0, column=1, padx=10, pady=10)

        from_unit_label = ttk.Label(frame, text="From:")
        from_unit_label.grid(row=1, column=0, padx=10, pady=10)
        from_unit = ttk.Combobox(frame, values=["cm", "m", "km", "in", "ft", "yd"], width=5)
        from_unit.grid(row=1, column=1, padx=10, pady=10)
        from_unit.current(0)

        to_unit_label = ttk.Label(frame, text="To:")
        to_unit_label.grid(row=2, column=0, padx=10, pady=10)
        to_unit = ttk.Combobox(frame, values=["cm", "m", "km", "in", "ft", "yd"], width=5)
        to_unit.grid(row=2, column=1, padx=10, pady=10)
        to_unit.current(3)

        result_label = ttk.Label(frame, text="Converted Length:")
        result_label.grid(row=3, column=0, padx=10, pady=10)
        result_entry = ttk.Entry(frame, width=20, state="readonly")
        result_entry.grid(row=3, column=1, padx=10, pady=10)

        # Conversion function
        def convert():
            try:
                value = float(entry.get())
                from_unit_value = from_unit.get()
                to_unit_value = to_unit.get()

                # Conversion logic for length
                converted_value = self.convert_length(value, from_unit_value, to_unit_value)

                result_entry.config(state="normal")
                result_entry.delete(0, tk.END)
                result_entry.insert(0, f"{converted_value:.4f}")
                result_entry.config(state="readonly")
            except ValueError:
                result_entry.config(state="normal")
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid input")
                result_entry.config(state="readonly")

        # Convert button
        convert_button = ttk.Button(frame, text="Convert", command=convert)
        convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Add the frame to the tab control
        self.tab_control.add(frame, text="Length")

    def convert_length(self, value, from_unit, to_unit):
        units = {
            "cm": 1,
            "m": 0.01,
            "km": 0.00001,
            "in": 0.393701,
            "ft": 0.0328084,
            "yd": 0.0109361
        }

        # Convert to base unit (cm)
        cm_value = value / units[from_unit]
        # Convert from base unit to target unit
        result = cm_value * units[to_unit]
        return result

    def weight_converter(self):
        frame = ttk.Frame(self.tab_control)
        frame.pack(fill="both", expand=1)

        # Labels and entry fields
        label = ttk.Label(frame, text="Enter Weight:")
        label.grid(row=0, column=0, padx=10, pady=10)
        entry = ttk.Entry(frame, width=20)
        entry.grid(row=0, column=1, padx=10, pady=10)

        from_unit_label = ttk.Label(frame, text="From:")
        from_unit_label.grid(row=1, column=0, padx=10, pady=10)
        from_unit = ttk.Combobox(frame, values=["g", "kg", "lb", "oz"], width=5)
        from_unit.grid(row=1, column=1, padx=10, pady=10)
        from_unit.current(0)

        to_unit_label = ttk.Label(frame, text="To:")
        to_unit_label.grid(row=2, column=0, padx=10, pady=10)
        to_unit = ttk.Combobox(frame, values=["g", "kg", "lb", "oz"], width=5)
        to_unit.grid(row=2, column=1, padx=10, pady=10)
        to_unit.current(1)

        result_label = ttk.Label(frame, text="Converted Weight:")
        result_label.grid(row=3, column=0, padx=10, pady=10)
        result_entry = ttk.Entry(frame, width=20, state="readonly")
        result_entry.grid(row=3, column=1, padx=10, pady=10)

        # Conversion function
        def convert():
            try:
                value = float(entry.get())
                from_unit_value = from_unit.get()
                to_unit_value = to_unit.get()

                # Conversion logic for weight
                converted_value = self.convert_weight(value, from_unit_value, to_unit_value)

                result_entry.config(state="normal")
                result_entry.delete(0, tk.END)
                result_entry.insert(0, f"{converted_value:.4f}")
                result_entry.config(state="readonly")
            except ValueError:
                result_entry.config(state="normal")
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid input")
                result_entry.config(state="readonly")

        # Convert button
        convert_button = ttk.Button(frame, text="Convert", command=convert)
        convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Add the frame to the tab control
        self.tab_control.add(frame, text="Weight")

    def convert_weight(self, value, from_unit, to_unit):
        units = {
            "g": 1,
            "kg": 0.001,
            "lb": 0.00220462,
            "oz": 0.035274
        }

        # Convert to base unit (g)
        g_value = value / units[from_unit]
        # Convert from base unit to target unit
        result = g_value * units[to_unit]
        return result

    def temperature_converter(self):
        frame = ttk.Frame(self.tab_control)
        frame.pack(fill="both", expand=1)

        # Labels and entry fields
        label = ttk.Label(frame, text="Enter Temperature:")
        label.grid(row=0, column=0, padx=10, pady=10)
        entry = ttk.Entry(frame, width=20)
        entry.grid(row=0, column=1, padx=10, pady=10)

        from_unit_label = ttk.Label(frame, text="From:")
        from_unit_label.grid(row=1, column=0, padx=10, pady=10)
        from_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], width=8)
        from_unit.grid(row=1, column=1, padx=10, pady=10)
        from_unit.current(0)

        to_unit_label = ttk.Label(frame, text="To:")
        to_unit_label.grid(row=2, column=0, padx=10, pady=10)
        to_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], width=8)
        to_unit.grid(row=2, column=1, padx=10, pady=10)
        to_unit.current(1)

        result_label = ttk.Label(frame, text="Converted Temperature:")
        result_label.grid(row=3, column=0, padx=10, pady=10)
        result_entry = ttk.Entry(frame, width=20, state="readonly")
        result_entry.grid(row=3, column=1, padx=10, pady=10)

        # Conversion function
        def convert():
            try:
                value = float(entry.get())
                from_unit_value = from_unit.get()
                to_unit_value = to_unit.get()

                # Conversion logic for temperature
                converted_value = self.convert_temperature(value, from_unit_value, to_unit_value)

                result_entry.config(state="normal")
                result_entry.delete(0, tk.END)
                result_entry.insert(0, f"{converted_value:.4f}")
                result_entry.config(state="readonly")
            except ValueError:
                result_entry.config(state="normal")
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid input")
                result_entry.config(state="readonly")

        # Convert button
        convert_button = ttk.Button(frame, text="Convert", command=convert)
        convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Add the frame to the tab control
        self.tab_control.add(frame, text="Temperature")

    def convert_temperature(self, value, from_unit, to_unit):
        conversions = {
            "Celsius to Fahrenheit": lambda x: x * 9/5 + 32,
            "Celsius to Kelvin": lambda x: x + 273.15,
            "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9,
            "Fahrenheit to Kelvin": lambda x: (x + 459.67) * 5/9,
            "Kelvin to Celsius": lambda x: x - 273.15,
            "Kelvin to Fahrenheit": lambda x: x * 9/5 - 459.67
        }

        key = f"{from_unit} to {to_unit}"
        if key in conversions:
            converted_value = conversions[key](value)
            return converted_value
        else:
            return None  # Conversion not defined

    def volume_converter(self):
        frame = ttk.Frame(self.tab_control)
        frame.pack(fill="both", expand=1)

        # Labels and entry fields
        label = ttk.Label(frame, text="Enter Volume:")
        label.grid(row=0, column=0, padx=10, pady=10)
        entry = ttk.Entry(frame, width=20)
        entry.grid(row=0, column=1, padx=10, pady=10)

        from_unit_label = ttk.Label(frame, text="From:")
        from_unit_label.grid(row=1, column=0, padx=10, pady=10)
        from_unit = ttk.Combobox(frame, values=["ml", "l", "cm^3", "m^3", "pt", "gal"], width=5)
        from_unit.grid(row=1, column=1, padx=10, pady=10)
        from_unit.current(0)

        to_unit_label = ttk.Label(frame, text="To:")
        to_unit_label.grid(row=2, column=0, padx=10, pady=10)
        to_unit = ttk.Combobox(frame, values=["ml", "l", "cm^3", "m^3", "pt", "gal"], width=5)
        to_unit.grid(row=2, column=1, padx=10, pady=10)
        to_unit.current(1)

        result_label = ttk.Label(frame, text="Converted Volume:")
        result_label.grid(row=3, column=0, padx=10, pady=10)
        result_entry = ttk.Entry(frame, width=20, state="readonly")
        result_entry.grid(row=3, column=1, padx=10, pady=10)

        # Conversion function
        def convert():
            try:
                value = float(entry.get())
                from_unit_value = from_unit.get()
                to_unit_value = to_unit.get()

                # Conversion logic for volume
                converted_value = self.convert_volume(value, from_unit_value, to_unit_value)

                result_entry.config(state="normal")
                result_entry.delete(0, tk.END)
                result_entry.insert(0, f"{converted_value:.4f}")
                result_entry.config(state="readonly")
            except ValueError:
                result_entry.config(state="normal")
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid input")
                result_entry.config(state="readonly")

        # Convert button
        convert_button = ttk.Button(frame, text="Convert", command=convert)
        convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Add the frame to the tab control
        self.tab_control.add(frame, text="Volume")

    def convert_volume(self, value, from_unit, to_unit):
        units = {
            "ml": 1,
            "l": 0.001,
            "cm^3": 1,
            "m^3": 0.000001,
            "pt": 0.00211338,
            "gal": 0.000264172
        }

        # Convert to base unit (ml or cm^3)
        base_unit_value = value / units[from_unit]
        # Convert from base unit to target unit
        result = base_unit_value * units[to_unit]
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
