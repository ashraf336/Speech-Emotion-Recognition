#READER CLASS
class Reader:
  def __init__(self, ravdess_path, crema_path, savee_path, tess_path):
    self.ravdess_path = ravdess_path
    self.crema_path = crema_path
    self.savee_path = savee_path
    self.tess_path = tess_path

  def readRavdess(self):
    ravdess_directory_list = os.listdir(self.ravdess_path)

    emotion_df = []

    for dir in ravdess_directory_list:
      actor = os.listdir(os.path.join(ravdess_path, dir))
      for wav in actor:
          info = wav.partition(".wav")[0].split("-")
          emotion = int(info[2])
          emotion_df.append((emotion, os.path.join(ravdess_path, dir, wav)))


    Ravdess_df = pd.DataFrame.from_dict(emotion_df)
    Ravdess_df.rename(columns={1 : "Path", 0 : "Emotion"}, inplace=True)
    Ravdess_df.Emotion.replace({1:'neutral', 2:'neutral', 3:'happy', 4:'sad', 5:'angry', 6:'fear', 7:'disgust', 8:'surprise'}, inplace=True)
    #print(Ravdess_df.head())
    return Ravdess_df

  def readCrema(self):
    emotion_df = []

    for wav in os.listdir(crema_path):
      info = wav.partition(".wav")[0].split("_")
      if info[2] == 'SAD':
        emotion_df.append(("sad", crema_path + "/" + wav))
      elif info[2] == 'ANG':
        emotion_df.append(("angry", crema_path + "/" + wav))
      elif info[2] == 'DIS':
        emotion_df.append(("disgust", crema_path + "/" + wav))
      elif info[2] == 'FEA':
        emotion_df.append(("fear", crema_path + "/" + wav))
      elif info[2] == 'HAP':
        emotion_df.append(("happy", crema_path + "/" + wav))
      elif info[2] == 'NEU':
        emotion_df.append(("neutral", crema_path + "/" + wav))
      else:
        emotion_df.append(("unknown", crema_path + "/" + wav))


    Crema_df = pd.DataFrame.from_dict(emotion_df)
    Crema_df.rename(columns={1 : "Path", 0 : "Emotion"}, inplace=True)

    #print(Crema_df.head())
    return Crema_df

  def readSavee(self):
    savee_directiory_list = os.listdir(savee_path)
    emotion_df = []
    for wav in savee_directiory_list:
      info = wav.partition(".wav")[0].split("_")[1].replace(r"[0-9]", "")
      emotion = re.split(r"[0-9]", info)[0]
      if emotion=='a':
        emotion_df.append(("angry", savee_path + "/" + wav))
      elif emotion=='d':
        emotion_df.append(("disgust", savee_path + "/" + wav))
      elif emotion=='f':
        emotion_df.append(("fear", savee_path + "/" + wav))
      elif emotion=='h':
        emotion_df.append(("happy", savee_path + "/" + wav))
      elif emotion=='n':
        emotion_df.append(("neutral", savee_path + "/" + wav))
      elif emotion=='sa':
        emotion_df.append(("sad", savee_path + "/" + wav))
      else:
        emotion_df.append(("surprise", savee_path + "/" + wav))

    Savee_df = pd.DataFrame.from_dict(emotion_df)
    Savee_df.rename(columns={1 : "Path", 0 : "Emotion"}, inplace=True)
    #print(Savee_df.head())
    return Savee_df

  def readTess(self):  
    tess_directory_list = os.listdir(tess_path)

    emotion_df = []

    for dir in tess_directory_list:
      for wav in os.listdir(os.path.join(tess_path, dir)):
        info = wav.partition(".wav")[0].split("_")
        emo = info[2]
        if emo == "ps":
            emotion_df.append(("surprise", os.path.join(tess_path, dir, wav)))
        else:
            emotion_df.append((emo, os.path.join(tess_path, dir, wav)))


    Tess_df = pd.DataFrame.from_dict(emotion_df)
    Tess_df.rename(columns={1 : "Path", 0 : "Emotion"}, inplace=True)

    #print(Tess_df.head())
    return Tess_df

  def read(self):
    ravdess_dataset = self.readRavdess()
    crema_dataset = self.readCrema()
    savee_dataset = self.readSavee()
    tess_dataset = self.readTess()
    return ravdess_dataset, crema_dataset, savee_dataset, tess_dataset
    
  def concatenate(self,ravdess_dataset,crema_dataset,savee_dataset,tess_dataset):
    concat_dataset = pd.concat([ravdess_dataset,crema_dataset,savee_dataset,tess_dataset], axis=0)
    print(concat_dataset.shape)
    return concat_dataset
