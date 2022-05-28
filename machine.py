from PIL import Image, ImageDraw


class Machine():
    def __init__(self,max):
        self.max = max
        self.Q = []
        self.addMachine()
        self.Name = 0
    def addMachine(self):
        self.Q.append([None for x in range(self.max)])


    def addTask(self,taskStartTime,taskWeight,taskName = None,row = 0):
        if taskName == None:
            taskName = self.Name
            self.Name += 1
        for x in range(taskStartTime, taskStartTime+taskWeight):
            if self.Q[row][x] != None:
                if len(self.Q) < row+2:
                    self.addMachine()
                return self.addTask(taskStartTime,taskWeight,taskName,row+1)

        for x in range(taskStartTime, taskStartTime + taskWeight):
            self.Q[row][x] = taskName

        return row



    def createImage(self,imageName):
        y = (len(self.Q) + 1) * 70
        x = self.max * 50
        img = Image.new('RGB', (x, y), color='#990099')
        draw = ImageDraw.Draw(img)
        for poziom in range(0,len(self.Q) + 2):
            draw.rectangle((0, (poziom) * 70 +2, img.size[0],(poziom) * 70-2) , fill ="#ffffff")
        for pion in range(0, self.max+1):

            draw.rectangle((pion * 50 + 2, 0,pion * 50 - 2, img.size[1]), fill="#ffffff")
            draw.text(((pion-1)*50+20,y-40 ), str(pion-1), align="left")

        start_x = 2
        start_y = 0
        end_x = 0
        end_y = 0
        self.Q = list(reversed(self.Q))
        for row in range(len(self.Q)):
            name = None
            start_x = 2
            for column in range(len(self.Q[row])):
                start_y = row * 70 + 2
                end_y = (row + 1) * 70 - 2
                end_x = (column) * 50 - 2
                if name == None:
                    name = self.Q[row][column]
                if name != self.Q[row][column] and name != None:
                    draw.rectangle((start_x, start_y, end_x, end_y), fill="#009933")
                    draw.text((int((end_x+start_x)/2)-5,round((start_y+end_y)/2)), str(name), align="left")
                    start_x = (column)*50+2
                    name = self.Q[row][column]
            if name != None:

                draw.rectangle((start_x, start_y, end_x+49, end_y), fill="#009933")
                draw.text((int((end_x + start_x) / 2)+20, round((start_y + end_y) / 2)), str(name), align="left")


        img.save(f'{imageName}.png')


    def __str__(self):
        self.createImage("próba")
        text = ""

        for x in range(len(self.Q)):
            for y in range(len(self.Q[x])):
                if self.Q[x][y] == None:
                    text += "-"
                else:
                    text += self.Q[x][y]
            text += "\n"


        return text








