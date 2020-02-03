# SYNERGO (In course)

In course

https://github.com/JeanBaptisteServais/try-rebuilt-Hand-skeletton (actual) + web site


<h1>Web Site Part</h1>

https://synergo2.herokuapp.com/ In progress

Documentation

<details>
  
![DIAGRAMME DE CLASSE TRUK SYNERGO 18 janvier](https://user-images.githubusercontent.com/54853371/72666930-e1310880-3a16-11ea-9966-915c4b2376c2.png)

</details>

Web site application

<details>
 
 Register
 
 Upload video
 
 Social media publications
  
</details>



<h1>Head</h1>

<details>

  Finish

  Requirements: (pip install -r requirements_head.txt)

</details>

<h1>Eyes</h1>
  
 <details>
  
  Finish
  Requirements: (pip install -r requirements_eyes.txt)
  
 </details>
  
<h1>Face</h1>

<details>
  
  Finish
  Requirements: (pip install -r requirements_face.txt)

</details>
  
<h1>Exterior Head</h1>

<details>

</details>

<h1>Hand</h1>

<details>

  - <h2>Hand detection</h2>
  
  model hand detection by:
  
  model skeletton by: 
  
  - <h2>Hand mask</h2>
    <em>Maybe finish</em>
    
  - <h2>Hand skeltton</h2>
  
![bb](https://user-images.githubusercontent.com/54853371/72691359-1592ea80-3b25-11ea-9539-861a3bfff08c.png)
    
  - <h2>no_finger_found</h2>
    <em>Maybe finish</em>
    
  - <h2> 1) thumb_location</h2>
  
 Here we recuperate skeletton points. We need to identify the position of the thumb because... we activilly search.
  
   ![thumb_localisation](https://user-images.githubusercontent.com/54853371/72765060-ddee7600-3bea-11ea-9ef5-49ce65c7c178.png)
    
For that we compare fingertip coordiantes


  - <h2>palm_analyse</h2>
    <em>Maybe finish</em>
    

   
  - <h2>Delete phax</h2>
  - <h2>Delete fingers</h2>
    
    

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
    
    D(t, m) = w * 0.574  < m < w * 0.775 or D(t, m) ∈ ]w * 0.574; w * 0.775[
    
    D(t, an) = in course
    
    D(t, a) = in course
    


And distance beetween finger's are egal to

    D(Fi, Fi+1) = (w * 0.295) * x
    
    where i ∈ N and i ∈ [1; 4] and x ∈ N and i ∈ [1; 4]
    
 

    or h * ... in course

    - where w, h are length and hight of hand position,
    
    - w if w > h and y if h > w 
    
    - w ∈ [114; 130] pxs
    
    - h  ∈ [81; 120] pxs


t = thumb; i = index; m = major; w, h = width, height of the contour; F = finger without thumb; x = finger number



</p>

</details>


  <h1>Fingers</h1>
  
 <details>
  
  - <h2>defintion_to_angle</h2>
      <em>In course</em>
  - <h2>position_of_the_finger</h2>
      <em>Maybe finish</em>
  - <h2>Identifiy fingers</h2>
    <em>Maybe finish</em>
  - <h2>similar_points_finger</h2>
      <em>Maybe finish</em>
  - <h2>courbure_du_doigt</h2>
      <em>In course</em>
  - <h2>sens finger</h2>
      <em>Maybe finish</em>
  - <h2>position des doigts les uns par apport aux autres</h2>  
      <em>Maybe finish</em>
  - <h2>space</h2>
      <em>Maybe finish</em>
  - <h2>position_beetween_fingers</h2>
      <em>Maybe finish</em>
  - <h2>length_of_fingers</h2>
      <em>Maybe finish</em>
  
  - <h2>Signes</h2>
      <em>In course</em>
  
  Requirements: (pip install -r requirements_hand.txt)

  to download :

</details>



<h1>Talk</h1>

<details>
</details>

<h1>Voice</h1>

<details>
</details>

<h1>Secret algo</h1>
<details>
</details>
