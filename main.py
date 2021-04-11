def test(input):
  """
  Function to test input string
  """
  #Change case of input to lower
  input = [x.lower() for x in input]

  #Course code
  crscd = input[2]
  #Course section
  crscsect = int(input[3])

  #Get student profile
  profile = getUserProfile(input[0], input[1])

  #State 1:
  if isinstance(profile, str):
    if profile == "wrngpass":
      return("Incorrect password")
    elif profile == "wrngmat":
      return("Incorrect matric no.")

  elif isinstance(profile, dict):
    courseinfo = getCourseInfo(crscd)

    #State 2:

    #Check if course code valid
    if isinstance(courseinfo, str):
      return("Invalid course code")
    
    if crscsect not in courseinfo['sections']:
      return("Invalid section")

    #Check if prequisites fulfilled
    crsPrereq = courseinfo['prereq']
    crsComp = profile['corscompl']
    if crsPrereq != []:
      for crs in crsPrereq:
        if crs not in crsComp:
          return("Pre-requisite unfulfilled.")
          
    #State 3:
    #Check if credit hour of new course exceeds maximum workload
    crntcredhr = profile['credHr']
    crscredhr = courseinfo['crdhr']
    if crntcredhr +  crscredhr > 24:
      return("Workload exceeded.")

    #State 4:
    return("Course added successfully.")

def getUserProfile(user, pwd):
  """
  Function to get user profile.
  """
  #Dictionary holding user information
  userDict = {'1814111':{'pass':'123456789', 
                         'credHr':18, 
                         'corscompl':['csc 3102','csc 2104', 'csc 1707']
                         },
              '1823431':{'pass':'987654321', 
                         'credHr':15, 
                         'corscompl':['csc 1103','csc 1401', 'csc 2706']
                         },
              '1729192':{'pass':'347436889', 
                         'credHr':19, 
                         'corscompl':['csc 2104','csc 1707', 'csc 1100']
                         }
              }
  
  #Check if user exists or password is wrong
  if user in userDict:
    if pwd == userDict[user]['pass']:
      return userDict[user]
    else:
      return "wrngpass"
  else:
    return "wrngmat"

def getCourseInfo(course):
  """
  Function to get course list for current semester
  """
  #Dictionaty holding course information
  courseList = {'csc 4101':{'prereq': ['csc 3102'],'sections':[1], 'crdhr': 3},
                'info 2401':{'prereq': ['csc 1100'],'sections':[1,2], 'crdhr': 3},
                'csc 1100':{'prereq': [],'sections':[1,2], 'crdhr': 3}}

  if course in courseList:
      return courseList[course]
  else:
      return "wrngcrs"

def main():
  #Input 1 (format: [matric no, passoword, course code, section no.])
  #Expected output: Input accepted (Course added) 
  input = ['1814111', '123456789', 'CSC 4101', '1']
  print('Input 1: ', test(input))

  #Input 2 (format: [matric no, passoword, course code, section no.])
  #Expected output: Input rejected (error) 
  input = ['1814111', '1234589', 'CSC 4101', '1']
  print('Input 2: ', test(input))

main()