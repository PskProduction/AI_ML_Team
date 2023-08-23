import pandas as pd
import os
import matplotlib.pyplot as plt


class DrawingPlots:
    def draw_plots(self, json_file_path):
        try:
            df = pd.read_json(json_file_path)
            plot_paths = []
            for column in df.columns:
                if pd.api.types.is_numeric_dtype(df[column]):
                    plt.figure(figsize=(12, 6))
                    plt.plot(df.index, df[column])
                    plt.title(column)
                    plt.xlabel('X axis')
                    plt.ylabel('Y axis')
                    plt.grid()

                    plot_filename = f'{column}.png'
                    if not os.path.exists(os.path.join(os.getcwd(), 'plots')):
                        os.mkdir(os.path.join(os.getcwd(), 'plots'))
                    plot_path = os.path.join(os.getcwd(), 'plots', plot_filename)
                    plt.savefig(plot_path)
                    plot_paths.append(plot_path)
                    plt.close()
            return plot_paths
        except Exception as e:
            print('Произошла ошибка: ', e)
            return []


json_file = 'deviation.json'
plotter = DrawingPlots()
plot_paths = plotter.draw_plots(json_file)
print('Plots saved to:', plot_paths)
