import PySimpleGUI as pa
import zip_creator


label1=pa.Text('Select File to Compress')
label2=pa.Text("Select the destination Folder")
text_box1=pa.InputText()
text_box2=pa.InputText()
file_folder=pa.FilesBrowse(key='folder')
button=pa.Button('Zip')
destination_folder=pa.FolderBrowse(key='Destination')
successful=pa.Text("")


window=pa.Window('File Compressor',layout=[[label1,text_box1,file_folder],[label2,text_box2,destination_folder],[button,successful]])

while True:
  event,value=window.read()
  print(event,value)
  filepaths=value['folder'].split(';')
  folder_path=(value['Destination'])
  print(folder_path)

  match event:
    case 'Zip':
      zip_creator.make_zip(filepaths, folder_path)
      if value['folder']=='':
        successful.update("select files and destination folder")
      else:
        successful.update("Compression successful")

    case pa.WIN_CLOSED:
      break

