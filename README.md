# SYNERGO (In course)

care not working, need to put it into file, and to put video_treatment for have dimensions

<strong>web site for behavior video analysis</strong> , we are curently writting the code for hand detection. The part of the web site, our speciality and the UML analysis's progress. The current code is not finish. We writting it on an another branch (another github)

<strong>In this web site i can: </strong> create my account, have acces to video analysis, make an analysis of my video (download it, wait 1-2 hours) and watch it ! Save my video, publish it on social media ...

<strong>In this web site i can: </strong> read the blog with jb approach (part for explain the code if we want)

<strong>Later: Mobile :</strong> register in real time video with my smarthphone, download it and have acces to the analysis (1-2 hours later).





![aa](https://user-images.githubusercontent.com/54853371/71028191-20fd8b00-210d-11ea-90fd-2ef5c299e2af.png)

<h1>Web Site Part</h1>

https://synergo2.herokuapp.com/ In progress


Finish = Doc and verify to apply

In course = writting code

<h1>Head</h1>

  Finish

  Requirements: (pip install -r requirements_head.txt)

<h1>Eyes</h1>
  
  Finish
  Requirements: (pip install -r requirements_eyes.txt)
  
  
<h1>Face</h1>

  Finish
  Requirements: (pip install -r requirements_face.txt)
  
  
<h1>Exterior Head</h1>


<h1>Hand</h1>

    

  - <h2>Hand detection</h2>
  
  model hand detection by:
  
  model skeletton by: 
  
  - <h2>Hand mask</h2>
    <em>Maybe finish</em>
    
  - <h2>Hand skeltton</h2>
  
    ![bb](https://user-images.githubusercontent.com/54853371/72481522-17923c00-37fb-11ea-9756-60bb727a06d4.png)
    
  - <h2>no_finger_found</h2>
    <em>Maybe finish</em>
    
  - <h2>hand_location</h2>
    <em>Maybe finish</em>
    
  - <h2>palm_analyse</h2>
    <em>Maybe finish</em>
    
  - <h2>reorganize_phax_position</h2>
    <em>Maybe finish</em>
    
  - <h2>reorganize_fingers</h2>
    <em>Maybe finish</em>

  - <h2>Identifiy fingers <em>In course</em></h2> 

  <p> Here we need to detect to which finger belongs its points for that we must define distances according to the direction of the hand that it is lying and thus in width, or on the contrary in length. For that use <stron>the contours</strong> of the hand.

<center>
  

![bb](https://user-images.githubusercontent.com/54853371/72475132-9337bd00-37ea-11ea-8c55-7e78e420502a.png)
![bb](https://user-images.githubusercontent.com/54853371/72475207-c37f5b80-37ea-11ea-964e-57548bee9ca1.png)
![bb](https://user-images.githubusercontent.com/54853371/72475315-f1fd3680-37ea-11ea-9c51-4f751bfbd02f.png)
![bb](https://user-images.githubusercontent.com/54853371/72475394-178a4000-37eb-11ea-8504-d2a79fe81990.png)

</center>

The model by ... detect almost always the thumb so we rely on the thumb. Next we search the next point of the thumb given above.

We have think thumb-index distance as:

    D(t, i) = i < w * 0.574 
    
    D(t, m) = w * 0.574  < m < w * 0.775 
    
    D(t, an) = in course
    
    D(t, a) = in course
    


And distance beetween finger's are egal to

    D(Fi, Fi+1) = (w * 0.295) * x 

    or h * ... in course

    - where w length of hand position and h is hight of hand position, w if w > h and y if h > w

t = thumb; i = index; m = major; w, h = width, height of the contour; F = finger without thumb; x = finger number



</p>


  - <h2>reorganize_finger</h2>
  
  - <h2>Identifiy fingers</h2>
  
  - <h2>Identifiy fingers</h2>
  
  - <h2>Identifiy fingers</h2>


  Requirements: (pip install -r requirements_hand.txt)

  to download :



<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

<h1>Talk</h1>

<h1>Voice</h1>

<h1>Secret algo</h1>
