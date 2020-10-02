import os
def createifdosentexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def move(foldername,files):
    for file in files:
        os.replace(file, f'{foldername}/{file}')
files=os.listdir()
createifdosentexist('images')
createifdosentexist('docs')
createifdosentexist('media')
createifdosentexist('programs')
createifdosentexist('others')
imgExts=['.png','.jpg','.jpeg']
docexts=['.docx','.txt','.doc','pdf']
programexts=['.py','.java','.html','.css','.js']
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docexts]
programs=[file for file in files if os.path.splitext(file)[1].lower() in programexts]
mediaexts=['.3g2','.flv','.mov','.mp3','.mp3']
medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaexts]
for file in files:
    ext=os.path.splitext(file)[1].lower()
others=[]
move("images", images)
move("media", medias)
move("docs", docs)
move('programs', programs)
move("others", others)
