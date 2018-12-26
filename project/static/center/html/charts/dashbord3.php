
<!DOCTYPE html>
<html class="no-js css-menubar" lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimal-ui">
    <meta name="description" content="bootstrap material admin template">
    <meta name="author" content="">
    
    <title>Idea Management System | Dashboard</title>
    
    <link rel="apple-touch-icon" href="../../assets/images/apple-touch-icon.png">
    <link rel="shortcut icon" href="../../assets/images/favicon.ico">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="../../../global/css/bootstrap.min.css">
    <link rel="stylesheet" href="../../../global/css/bootstrap-extend.min.css">
    <link rel="stylesheet" href="../../assets/css/site.min.css">
    
    <!-- Plugins -->
    <link rel="stylesheet" href="../../../global/vendor/animsition/animsition.css">
    <link rel="stylesheet" href="../../../global/vendor/asscrollable/asScrollable.css">
    <link rel="stylesheet" href="../../../global/vendor/switchery/switchery.css">
    <link rel="stylesheet" href="../../../global/vendor/intro-js/introjs.css">
    <link rel="stylesheet" href="../../../global/vendor/slidepanel/slidePanel.css">
    <link rel="stylesheet" href="../../../global/vendor/flag-icon-css/flag-icon.css">
    <link rel="stylesheet" href="../../../global/vendor/waves/waves.css">
        <link rel="stylesheet" href="../../../global/vendor/chartist/chartist.css">
        <link rel="stylesheet" href="../../../global/vendor/chartist-plugin-tooltip/chartist-plugin-tooltip.css">
        <link rel="stylesheet" href="../../assets/examples/css/charts/chartist.css">
         <link rel="stylesheet" href="../../assets/examples/css/dashboard/v1.css">
           <link rel="stylesheet" href="../../../global/vendor/jvectormap/jquery-jvectormap.css">
    
    
    <!-- Fonts -->
    <link rel="stylesheet" href="../../../global/fonts/material-design/material-design.min.css">
    <link rel="stylesheet" href="../../../global/fonts/brand-icons/brand-icons.min.css">
    <link rel='stylesheet' href='http://fonts.googleapis.com/css?family=Roboto:300,400,500,300italic'>
    
    <!--[if lt IE 9]>
    <script src="../../../global/vendor/html5shiv/html5shiv.min.js"></script>
    <![endif]-->
    
    <!--[if lt IE 10]>
    <script src="../../../global/vendor/media-match/media.match.min.js"></script>
    <script src="../../../global/vendor/respond/respond.min.js"></script>
    <![endif]-->
    
    <!-- Scripts -->
    <script src="../../../global/vendor/breakpoints/breakpoints.js"></script>
    <script>
      Breakpoints();
    </script>
  </head>
  <body class="animsition">
    <!--[if lt IE 8]>
        <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
    <![endif]-->

    <nav class="site-navbar navbar navbar-default navbar-fixed-top navbar-mega navbar-inverse"
      role="navigation">
    
      <div class="navbar-header">
        <button type="button" class="navbar-toggler hamburger hamburger-close navbar-toggler-left hided"
          data-toggle="menubar">
          <span class="sr-only">Toggle navigation</span>
          <span class="hamburger-bar"></span>
        </button>
        <button type="button" class="navbar-toggler collapsed" data-target="#site-navbar-collapse"
          data-toggle="collapse">
          <i class="icon md-more" aria-hidden="true"></i>
        </button>
        <div class="navbar-brand navbar-brand-center site-gridmenu-toggle" data-toggle="gridmenu">
          <img class="navbar-brand-logo" src="../../assets/images/logo.png" title="Remark">
          <span class="navbar-brand-text hidden-xs-down"> Remark</span>
        </div>
        <button type="button" class="navbar-toggler collapsed" data-target="#site-navbar-search"
          data-toggle="collapse">
          <span class="sr-only">Toggle Search</span>
          <i class="icon md-search" aria-hidden="true"></i>
        </button>
      </div>
    
      <div class="navbar-container container-fluid">
        <!-- Navbar Collapse -->
        <div class="collapse navbar-collapse navbar-collapse-toolbar" id="site-navbar-collapse">
          <!-- Navbar Toolbar -->
          <ul class="nav navbar-toolbar">
            <li class="nav-item hidden-float" id="toggleMenubar">
              <a class="nav-link" data-toggle="menubar" href="#" role="button">
                <i class="icon hamburger hamburger-arrow-left">
                  <span class="sr-only">Toggle menubar</span>
                  <span class="hamburger-bar"></span>
                </i>
                  <span class="navbar-brand-text hidden-xs-down"><strong> My Account</strong></span>

              </a>
            </li>
             
            <li class="nav-item hidden-sm-down" id="toggleFullscreen">
              <a class="nav-link icon icon-fullscreen" data-toggle="fullscreen" href="#" role="button">
                <span class="sr-only">Toggle fullscreen</span>
              </a>
            </li>
            <li class="nav-item hidden-float">
              <a class="nav-link icon md-search" data-toggle="collapse" href="#" data-target="#site-navbar-search"
                role="button">
                <span class="sr-only">Toggle Search</span>
              </a>
            </li>
            
          </ul>
          <!-- End Navbar Toolbar -->
    
          <!-- Navbar Toolbar Right -->
          <ul class="nav navbar-toolbar navbar-right navbar-toolbar-right">
            <li class="nav-item dropdown">
             <!-- <a class="nav-link" data-toggle="dropdown" href="javascript:void(0)" data-animation="scale-up"
                aria-expanded="false" role="button">-->
                 
              <a class="nav-link" data-toggle="dropdown" href="#" aria-expanded="false" data-animation="fade"
                 role="button"> <i class="icon md-plus" aria-hidden="true">&nbsp;&nbsp;<span></span>Create Group</i></a>

                    <!--<span class="navbar-brand-text hidden-xs-down">
                  <strong>Create Group</strong></span>-->
                
              </a>
              
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link navbar-avatar" data-toggle="dropdown" href="#" aria-expanded="false"
                data-animation="scale-up" role="button">
                <span class="avatar avatar-online">
                  <img src="../../../global/portraits/5.jpg" alt="...">
                  <i></i>
                </span>
              </a>
              <div class="dropdown-menu" role="menu">
                <a class="dropdown-item" href="javascript:void(0)" role="menuitem"><i class="icon md-account" aria-hidden="true"></i> Profile</a>
                
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="javascript:void(0)" role="menuitem"><i class="icon md-power" aria-hidden="true"></i> Logout</a>
              </div>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link" data-toggle="dropdown" href="javascript:void(0)" title="Notifications"
                aria-expanded="false" data-animation="scale-up" role="button">
                <i class="icon md-notifications" aria-hidden="true"></i>
                <span class="badge badge-pill badge-danger up">5</span>
              </a>
              <div class="dropdown-menu dropdown-menu-right dropdown-menu-media" role="menu">
                <div class="dropdown-menu-header">
                  <h5>NOTIFICATIONS</h5>
                  <span class="badge badge-round badge-danger">New 5</span>
                </div>
    
                <div class="list-group">
                  <div data-role="container">
                    <div data-role="content">
                      <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                        <div class="media">
                          <div class="pr-10">
                            <i class="icon md-receipt bg-red-600 white icon-circle" aria-hidden="true"></i>
                          </div>
                          <div class="media-body">
                            <h6 class="media-heading">A new order has been placed</h6>
                            <time class="media-meta" datetime="2017-06-12T20:50:48+08:00">5 hours ago</time>
                          </div>
                        </div>
                      </a>
                      <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                        <div class="media">
                          <div class="pr-10">
                            <i class="icon md-account bg-green-600 white icon-circle" aria-hidden="true"></i>
                          </div>
                          <div class="media-body">
                            <h6 class="media-heading">Completed the task</h6>
                            <time class="media-meta" datetime="2017-06-11T18:29:20+08:00">2 days ago</time>
                          </div>
                        </div>
                      </a>
                      <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                        <div class="media">
                          <div class="pr-10">
                            <i class="icon md-settings bg-red-600 white icon-circle" aria-hidden="true"></i>
                          </div>
                          <div class="media-body">
                            <h6 class="media-heading">Settings updated</h6>
                            <time class="media-meta" datetime="2017-06-11T14:05:00+08:00">2 days ago</time>
                          </div>
                        </div>
                      </a>
                      <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                        <div class="media">
                          <div class="pr-10">
                            <i class="icon md-calendar bg-blue-600 white icon-circle" aria-hidden="true"></i>
                          </div>
                          <div class="media-body">
                            <h6 class="media-heading">Event started</h6>
                            <time class="media-meta" datetime="2017-06-10T13:50:18+08:00">3 days ago</time>
                          </div>
                        </div>
                      </a>
                      <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                        <div class="media">
                          <div class="pr-10">
                            <i class="icon md-comment bg-orange-600 white icon-circle" aria-hidden="true"></i>
                          </div>
                          <div class="media-body">
                            <h6 class="media-heading">Message received</h6>
                            <time class="media-meta" datetime="2017-06-10T12:34:48+08:00">3 days ago</time>
                          </div>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
                <div class="dropdown-menu-footer">
                  <a class="dropdown-menu-footer-btn" href="javascript:void(0)" role="button">
                    <i class="icon md-settings" aria-hidden="true"></i>
                  </a>
                  <a class="dropdown-item" href="javascript:void(0)" role="menuitem">
                    All notifications
                  </a>
                </div>
              </div>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link" data-toggle="dropdown" href="javascript:void(0)" title="Messages"
                aria-expanded="false" data-animation="scale-up" role="button">
                <i class="icon md-email" aria-hidden="true"></i>
                <span class="badge badge-pill badge-info up">3</span>
              </a>
              <div class="dropdown-menu dropdown-menu-right dropdown-menu-media" role="menu">
                <div class="dropdown-menu-header" role="presentation">
                  <h5>MESSAGES</h5>
                  <span class="badge badge-round badge-info">New 3</span>
                </div>
    
                <div class="list-group" role="presentation">
                  <div data-role="container">
                    <div data-role="content">
                      <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                        <div class="media">
                          <div class="pr-10">
                            <span class="avatar avatar-sm avatar-online">
                              <img src="../../../global/portraits/2.jpg" alt="..." />
                              <i></i>
                            </span>
                          </div>
                          <div class="media-body">
                            <h6 class="media-heading">Mary Adams</h6>
                            <div class="media-meta">
                              <time datetime="2017-06-17T20:22:05+08:00">30 minutes ago</time>
                            </div>
                            <div class="media-detail">Anyways, i would like just do it</div>
                          </div>
                        </div>
                      </a>
                      <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                        <div class="media">
                          <div class="pr-10">
                            <span class="avatar avatar-sm avatar-off">
                              <img src="../../../global/portraits/3.jpg" alt="..." />
                              <i></i>
                            </span>
                          </div>
                          <div class="media-body">
                            <h6 class="media-heading">Caleb Richards</h6>
                            <div class="media-meta">
                              <time datetime="2017-06-17T12:30:30+08:00">12 hours ago</time>
                            </div>
                            <div class="media-detail">I checheck the document. But there seems</div>
                          </div>
                        </div>
                      </a>
                      <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                        <div class="media">
                          <div class="pr-10">
                            <span class="avatar avatar-sm avatar-busy">
                              <img src="../../../global/portraits/4.jpg" alt="..." />
                              <i></i>
                            </span>
                          </div>
                          <div class="media-body">
                            <h6 class="media-heading">June Lane</h6>
                            <div class="media-meta">
                              <time datetime="2017-06-16T18:38:40+08:00">2 days ago</time>
                            </div>
                            <div class="media-detail">Lorem ipsum Id consectetur et minim</div>
                          </div>
                        </div>
                      </a>
                      <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                        <div class="media">
                          <div class="pr-10">
                            <span class="avatar avatar-sm avatar-away">
                              <img src="../../../global/portraits/5.jpg" alt="..." />
                              <i></i>
                            </span>
                          </div>
                          <div class="media-body">
                            <h6 class="media-heading">Edward Fletcher</h6>
                            <div class="media-meta">
                              <time datetime="2017-06-15T20:34:48+08:00">3 days ago</time>
                            </div>
                            <div class="media-detail">Dolor et irure cupidatat commodo nostrud nostrud.</div>
                          </div>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
                <div class="dropdown-menu-footer" role="presentation">
                  <a class="dropdown-menu-footer-btn" href="javascript:void(0)" role="button">
                    <i class="icon md-settings" aria-hidden="true"></i>
                  </a>
                  <a class="dropdown-item" href="javascript:void(0)" role="menuitem">
                    See all messages
                  </a>
                </div>
              </div>
            </li>
            <li class="nav-item" id="toggleChat">
              <a class="nav-link" data-toggle="site-sidebar" href="javascript:void(0)" title="Chat"
                data-url="../site-sidebar.tpl">
                <i class="icon md-comment" aria-hidden="true"></i>
              </a>
            </li>
          </ul>
          <!-- End Navbar Toolbar Right -->
    
          <div class="navbar-brand navbar-brand-center">
              <a href="#" style="color:white;">
              <img class="navbar-brand-logo navbar-brand-logo-normal" src="../../assets/images/logo.png"
                title="Remark">
              <img class="navbar-brand-logo navbar-brand-logo-special" src="../../assets/images/logo-colored.png"
                title="Remark">
              Idea Management System
            </a>
          </div>
        </div>
        <!-- End Navbar Collapse -->
    
        <!-- Site Navbar Seach -->
        <div class="collapse navbar-search-overlap" id="site-navbar-search">
          <form role="search">
            <div class="form-group">
              <div class="input-search">
                <i class="input-search-icon md-search" aria-hidden="true"></i>
                <input type="text" class="form-control" name="site-search" placeholder="Search...">
                <button type="button" class="input-search-close icon md-close" data-target="#site-navbar-search"
                  data-toggle="collapse" aria-label="Close"></button>
              </div>
            </div>
          </form>
        </div>
        <!-- End Site Navbar Seach -->
      </div>
    </nav>    <div class="site-menubar">
      <div class="site-menubar-header">
        <div class="cover overlay">
          <img class="cover-image" src="../../assets//examples/images/dashboard-header.jpg"
            alt="...">
          <div class="overlay-panel vertical-align overlay-background">
            <div class="vertical-align-middle">
              <a class="avatar avatar-lg" href="javascript:void(0)">
                <img src="../../../global/portraits/1.jpg" alt="">
              </a>
              <div class="site-menubar-info">
                <h5 class="site-menubar-user">Sandeep</h5>
                <p class="site-menubar-email">sandeep@pes.edu</p>
                <p class="site-menubar-email">900000000</p>
              </div>
            </div>
          </div>
        </div>
      </div>  <div class="site-menubar-body">
        <div>
          <div>
            <ul class="site-menu" data-plugin="menu">
              <li class="site-menu-item">
                <a class="animsition-link" href="../charts/dashbord3.php">
                        <i class="site-menu-icon md-view-dashboard" aria-hidden="true"></i>
                        <span class="site-menu-title">Dashboard</span>
                    </a>
              </li>
              
            </ul>  </div>
        </div>
      </div>
    </div>

    <!-- Page -->
      <div class="page">
      <div class="page-content container-fluid">
        <div class="row" data-plugin="matchHeight" data-by-row="true">
          <div class="col-xl-3 col-md-6">
            <!-- Widget Linearea One-->
            <div class="card card-shadow" id="widgetLineareaOne">
              <div class="card-block p-20 pt-10">
                <div class="clearfix">
                  <div class="grey-800 float-left py-10">
                    <i class="icon md-account grey-600 font-size-24 vertical-align-bottom mr-5"></i>                    User
                  </div>
                  <span class="float-right grey-700 font-size-30">1,253</span>
                </div>
                <div class="mb-20 grey-500">
                  <i class="icon md-long-arrow-up green-500 font-size-16"></i>15% From this yesterday
                </div>
                  <div class="ct-chart h-50">
             <svg xmlns:ct="http://gionkunz.github.com/chartist-js/ct" width="100%" height="100%" class="ct-chart-line" style="width: 100%; height: 100%;"><g class="ct-grids"></g><g><g class="ct-series ct-series-a"><path d="M0,50L0,50C10.821,45.833,21.643,43.056,32.464,37.5C43.286,31.944,54.107,12.5,64.929,12.5C75.75,12.5,86.571,25,97.393,25C108.214,25,119.036,6.25,129.857,6.25C140.679,6.25,151.5,35,162.321,35C173.143,35,183.964,31.25,194.786,31.25C205.607,31.25,216.429,43.75,227.25,50L227.25,50Z" class="ct-area"></path></g></g><g class="ct-labels"></g></svg>         
                  </div>
              </div>
            </div>
            <!-- End Widget Linearea One -->
          </div>
          <div class="col-xl-3 col-md-6">
            <!-- Widget Linearea Two -->
            <div class="card card-shadow" id="widgetLineareaTwo">
              <div class="card-block p-20 pt-10">
                <div class="clearfix">
                  <div class="grey-800 float-left py-10">
                    <i class="icon md-flash grey-600 font-size-24 vertical-align-bottom mr-5"></i>VISITS
                  </div>
                  <span class="float-right grey-700 font-size-30">2,425</span>
                </div>
                <div class="mb-20 grey-500">
                  <i class="icon md-long-arrow-up green-500 font-size-16"></i>34.2% From this week
                </div>
                  <div class="ct-chart h-50">
                      <svg xmlns:ct="http://gionkunz.github.com/chartist-js/ct" width="100%" height="100%" class="ct-chart-line" style="width: 100%; height: 100%;"><g class="ct-grids"></g><g><g class="ct-series ct-series-a"><path d="M0,50L0,50C9.469,47.917,18.938,46.97,28.406,43.75C37.875,40.53,47.344,22.5,56.813,22.5C66.281,22.5,75.75,25,85.219,25C94.688,25,104.156,15,113.625,15C123.094,15,132.563,21.25,142.031,21.25C151.5,21.25,160.969,8.75,170.438,8.75C179.906,8.75,189.375,13.699,198.844,18.75C208.313,23.801,217.781,39.583,227.25,50L227.25,50Z" class="ct-area"></path></g></g><g class="ct-labels"></g></svg>
                  </div>
              </div>
            </div>
            <!-- End Widget Linearea Two -->
          </div>
          <div class="col-xl-3 col-md-6">
            <!-- Widget Linearea Three -->
            <div class="card card-shadow" id="widgetLineareaThree">
              <div class="card-block p-20 pt-10">
                <div class="clearfix">
                  <div class="grey-800 float-left py-10">
                    <i class="icon md-chart grey-600 font-size-24 vertical-align-bottom mr-5"></i>Total Clicks
                  </div>
                  <span class="float-right grey-700 font-size-30">1,864</span>
                </div>
                <div class="mb-20 grey-500">
                  <i class="icon md-long-arrow-down red-500 font-size-16"></i>15% From this yesterday
                </div>
                  <div class="ct-chart h-50">
                      <svg xmlns:ct="http://gionkunz.github.com/chartist-js/ct" width="100%" height="100%" class="ct-chart-line" style="width: 100%; height: 100%;"><g class="ct-grids"></g><g><g class="ct-series ct-series-a"><path d="M0,50L0,50C10.821,41.667,21.643,25,32.464,25C43.286,25,54.107,31.25,64.929,31.25C75.75,31.25,86.571,6.25,97.393,6.25C108.214,6.25,119.036,22.5,129.857,22.5C140.679,22.5,151.5,12.5,162.321,12.5C173.143,12.5,183.964,35.111,194.786,40C205.607,44.889,216.429,46.667,227.25,50L227.25,50Z" class="ct-area"></path></g></g><g class="ct-labels"></g></svg>
                  </div>
              </div>
            </div>
            <!-- End Widget Linearea Three -->
          </div>
          <div class="col-xl-3 col-md-6">
            <!-- Widget Linearea Four -->
            <div class="card card-shadow" id="widgetLineareaFour">
              <div class="card-block p-20 pt-10">
                <div class="clearfix">
                  <div class="grey-800 float-left py-10">
                    <i class="icon md-view-list grey-600 font-size-24 vertical-align-bottom mr-5"></i>                    Items
                  </div>
                  <span class="float-right grey-700 font-size-30">845</span>
                </div>
                <div class="mb-20 grey-500">
                  <i class="icon md-long-arrow-up green-500 font-size-16"></i>18.4% From this yesterday
                </div>
                  <div class="ct-chart h-50">
                      <svg xmlns:ct="http://gionkunz.github.com/chartist-js/ct" width="100%" height="100%" class="ct-chart-line" style="width: 100%; height: 100%;"><g class="ct-grids"></g><g><g class="ct-series ct-series-a"><path d="M0,50L0,50C9.469,45,18.938,40,28.406,35C37.875,30,47.344,20.769,56.813,20C66.281,19.231,75.75,19.508,85.219,18.75C94.688,17.992,104.156,6.25,113.625,6.25C123.094,6.25,132.563,25,142.031,25C151.5,25,160.969,18.75,170.438,18.75C179.906,18.75,189.375,29.8,198.844,35C208.313,40.2,217.781,45,227.25,50L227.25,50Z" class="ct-area"></path></g></g><g class="ct-labels"></g></svg>
                  </div>
              </div>
            </div>
            <!-- End Widget Linearea Four -->
          </div>      
        
      <div class="page-content container-fluid">
        <!-- Panel line css animation Chart -->
        <div class="panel">
        
          <div class="panel-body">
            <!-- Example css animation Chart -->
            <!-- Panel Column Toggle -->
           <div class="col-lg-6 col-sm-12 masonry-item">
              <header class="panel-heading">
                <h3 class="panel-title">Table</h3>
              </header>
              <div class="panel-body" >
                <table class="tablesaw table-striped table-bordered" data-tablesaw-mode="columntoggle"
                 style="width:500px;height:300px;" >
                    
                  <thead>
                     
                      <tr>
                          <th colspan="2" style="height:40px;"><strong> <center>Group He is a part of</strong></center> </th></tr>
                      <tr>
                          <th data-tablesaw-priority="3"><strong>As Member</strong></th>
                          <th data-tablesaw-priority="persist"><strong>As Manager</strong></th>
                     
                    </tr>
                  </thead>
                  <tbody style=";">
                    <tr>
                      <th><a href="javascript:void(0)" data-rel="external">Santhosh</a></th>
                      <td><a href="javascript:void(0)" data-rel="external">Santhosh</a></td>
                      
                    </tr>
                    <tr>
                      <th><a href="javascript:void(0)" data-rel="external">Roshan</a></th>
                      <td><a href="javascript:void(0)" data-rel="external">Roshan</a></td>
                      
                    </tr>
                    <tr>
                      <th><a href="javascript:void(0)" data-rel="external">Suraksha</a></th>
                      <td><a href="javascript:void(0)" data-rel="external">Suraksha</a></td>
                      
                    </tr>
                    <tr>
                      <th><a href="javascript:void(0)" data-rel="external">Pavan</a></th>
                      <td><a href="javascript:void(0)" data-rel="external">Pavan</a></td>
                     
                    </tr>
                    <tr>
                        <th><a href="javascript:void(0)" data-rel="external">Kavya</a></th>
                      <td><a href="javascript:void(0)" data-rel="external">Kavya</a></td>
                      
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- End Panel Column Toggle -->
          </div>
            
            
                <div class="col-lg-6  masonry-item">
                  <div class="example">
                    <div class="ct-chart ct-golden-section" id="exampleLineAnimation" style="position:relative; left:600px;bottom:380px"></div>
                  </div>
                </div>
            
            
            <!-- End Example css animation Chart -->
          </div>
        </div>
        </div>
        <!-- End Panel Pie -->
        <!-- Panel Line -->
       
        <!-- End Panel Pie -->
        </div>
      </div>
   
    <!-- End Page -->


    <!-- Footer -->
    <footer class="site-footer">
      <div class="site-footer-legal">© 2018 <a href="http://themeforest.net/item/remark-responsive-bootstrap-admin-template/11989202">Remark</a></div>
      <div class="site-footer-right">
        Crafted with <i class="red-600 icon md-favorite"></i> by <a href="https://themeforest.net/user/creation-studio">Creation Studio</a>
      </div>
    </footer>
    <!-- Core  -->
    <script src="../../../global/vendor/babel-external-helpers/babel-external-helpers.js"></script>
    <script src="../../../global/vendor/jquery/jquery.js"></script>
    <script src="../../../global/vendor/popper-js/umd/popper.min.js"></script>
    <script src="../../../global/vendor/bootstrap/bootstrap.js"></script>
    <script src="../../../global/vendor/animsition/animsition.js"></script>
    <script src="../../../global/vendor/mousewheel/jquery.mousewheel.js"></script>
    <script src="../../../global/vendor/asscrollbar/jquery-asScrollbar.js"></script>
    <script src="../../../global/vendor/asscrollable/jquery-asScrollable.js"></script>
    <script src="../../../global/vendor/waves/waves.js"></script>
    
    <!-- Plugins -->
    <script src="../../../global/vendor/switchery/switchery.js"></script>
    <script src="../../../global/vendor/intro-js/intro.js"></script>
    <script src="../../../global/vendor/screenfull/screenfull.js"></script>
    <script src="../../../global/vendor/slidepanel/jquery-slidePanel.js"></script>
        <script src="../../../global/vendor/chartist/chartist.js"></script>
        <script src="../../../global/vendor/chartist-plugin-tooltip/chartist-plugin-tooltip.js"></script>
    
    <!-- Scripts -->
    <script src="../../../global/js/Component.js"></script>
    <script src="../../../global/js/Plugin.js"></script>
    <script src="../../../global/js/Base.js"></script>
    <script src="../../../global/js/Config.js"></script>
    
    <script src="../../assets/js/Section/Menubar.js"></script>
    <script src="../../assets/js/Section/Sidebar.js"></script>
    <script src="../../assets/js/Section/PageAside.js"></script>
    <script src="../../assets/js/Plugin/menu.js"></script>
    
    <!-- Config -->
    <script src="../../../global/js/config/colors.js"></script>
    <script src="../../assets/js/config/tour.js"></script>
    <script>Config.set('assets', '../../assets');</script>
    
    <!-- Page -->
    <script src="../../assets/js/Site.js"></script>
    <script src="../../../global/js/Plugin/asscrollable.js"></script>
    <script src="../../../global/js/Plugin/slidepanel.js"></script>
    <script src="../../../global/js/Plugin/switchery.js"></script>
    
        <script src="../../assets/examples/js/charts/chartist.js"></script>
  </body>
</html>
