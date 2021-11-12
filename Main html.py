<!DOCTYPE html>

{% import "bootstrap/wtf.html" as wtf %}

<html lang="en">

<head>

    <meta charset="UTF-8">

    <title>EVT</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">

    <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" rel="stylesheet">

    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>

    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

</head>

<body>

<div class="jumbotron text-center">

  <h1>Hey, Welcome</h1>

  <p>ASK the question, I'll try to answer them</p>

</div>

<section>

    <div class="container">

        <div class="d-flex justify-content-between">

            <div class=p-1></div>

            <div class=p-1>

                <h1 class="display-5">What would you like to Ask Today?</h1>

               <form method="post">

                   <div class="form-group">

                       {{ wtf.quick_form(form)}}

                         <small id="QueryHelp" class="form-text text-muted">Example: What is Python</small>

                   </div>

<!--                   <button type="submit" class="btn btn-primary">Submit</button>-->

               </form>

            </div>

            <div class="p-1"></div>

        </div>

    </div>

</section>

  {% if result %}

 <section>

       <div class="container">

        <div class="row justify-content-center">

            <h3>Top RESULT</h3>

            <div class="p-1">{{result}}</div>

        </div>

       </div>

 </section>

 {% endif %}

<section style="margin:100;">

</section>

</body>

</html>

        
