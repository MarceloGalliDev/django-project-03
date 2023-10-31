# flake8: noqa
# pylint: disable=all

from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'


class DadosJSONView(BaseLineChartView):
    
    """Return 12 labels for the x-axis."""
    def get_labels(self):
        labels = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "November",
            "December"
        ]
        return labels

    """Return names of datasets."""
    def get_providers(self):
        datasets = [
            "Carnes",
            "Vegetais",
            "Legumes",
            "Frutas",
            "Doces",
        ]
        
        return datasets
    
    """
    Return 5 datasets to plot.
    Cada linha é um dataset
    Cada coluna é um label

    12 colunas e 5 linhas
    """
    def get_data(self):
        linhas = 5
        colunas = 12

        data_chart = []
        for l in range(linhas):
            dataset = [randint(0, 200) for c in range(colunas)]
            data_chart.append(dataset)
        return data_chart
