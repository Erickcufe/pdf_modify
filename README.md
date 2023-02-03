# pdf_modify


```conda create -n python2.7_pdf python=2.7.13```

```conda activate python2.7_pdf```

```pip install PyPDF2 reportlab ```

```conda env create --name python2.7_pdf --file=python2.7_pdf.yml```

## Intrucciones de uso 

Primero genera un envoriment con conda en tu terminal usando el archivo `python2.7_pdf.yml`.

```conda env create --name python2.7_pdf --file=python2.7_pdf.yml```

Una vez que el ambiente esta generado, usa ```conda activate python2.7_pdf```.

La carpeta donde se encuentres tus archivos PDF debe tener el nombre de **pdfs_firmar**.

Ahora solo ejecuta el archivo **pdf_mod.py** usando el comando `python pdf_mod.py`. Y listo. Recuerda en tu PATH o directorio donde estas trabajando deben existir los siguientes archivos que puedes descargar desde este repositorio:

1. python2.7_pdf.yml
2. pdf_mod.py
3. Una carpeta con el nombre **pdfs_firmar** donde se localicen solo los pdf.
