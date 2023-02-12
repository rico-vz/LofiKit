import os

ROOT_DIR = './public/assets/'
DEST_DIR = './src/components/'

for folder_name in ['music', 'effects']:
  subfolder_name = 'effects' if folder_name == 'effects' else 'music'
  path = f"{ROOT_DIR}{folder_name}/"
  if folder_name == 'music':
    for genre in os.listdir(path):
      songs = [f"/assets/{subfolder_name}/{genre}/{song}" for song in os.listdir(f"{path}{genre}")]
      with open(f"{DEST_DIR}{genre}Songs.js", 'w') as f:
        f.write("export default [\n")
        for song in songs:
          f.write(f"  '{song}',\n")
        f.write("];\n")
  else:
    effects = [f"/assets/{subfolder_name}/{effect}" for effect in os.listdir(path)]
    with open(f"{DEST_DIR}effects.js", 'w') as f:
      f.write("export default [\n")
      for effect in effects:
        f.write(f"  '{effect}',\n")
      f.write("];\n")
