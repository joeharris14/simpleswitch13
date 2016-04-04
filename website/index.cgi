#!/usr/bin/perl
use CGI qw/:all/;
use CGI::Cookie;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

sub main() {
  open F, "<","monitor.txt" or die;
  @lines = <F>;
  print "Content-type: text/html\n\n";
  print <<eof;
  <html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
      <meta name="description" content="">
      <meta name="author" content="">
      <link rel="icon" href="/img/favicon.png">

      <title>SimpleSwitch13</title>

      <!-- Bootstrap core CSS -->
      <!-- Latest compiled and minified CSS -->
      <link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

      <!-- Custom styles for this template -->
      <link href="/bootstrap/css/dashboard.css" rel="stylesheet">

      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->
    </head>

    <body>
      <nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container-fluid">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">SS13</a>
          </div>
          <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav navbar-right">
              <li><a href="#">Dashboard</a></li>
              <li><a href="#">Settings</a></li>
              <li><a href="#">Profile</a></li>
              <li><a href="#">Help</a></li>
            </ul>
            <form class="navbar-form navbar-right">
              <input type="text" class="form-control" placeholder="Search...">
            </form>
          </div>
        </div>
      </nav>

      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-3 col-md-2 sidebar">
            <ul class="nav nav-sidebar">
              <li class="active"><a href="#">Overview <span class="sr-only">(current)</span></a></li>
              <li><a href="#">Reports</a></li>
              <li><a href="#">Analytics</a></li>
              <li><a href="#">Export</a></li>
            </ul>
            <ul class="nav nav-sidebar">
              <li><a href="">Nav item</a></li>
              <li><a href="">Nav item again</a></li>
              <li><a href="">One more nav</a></li>
              <li><a href="">Another nav item</a></li>
              <li><a href="">More navigation</a></li>
            </ul>
            <ul class="nav nav-sidebar">
              <li><a href="">Nav item again</a></li>
              <li><a href="">One more nav</a></li>
              <li><a href="">Another nav item</a></li>
            </ul>
          </div>
          <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
eof
# $num = 0;
#   foreach my $line (@lines) {
#     my @values = split ' ', $line;
#     print "$values[0] $values[1] $values[2] $values[3]<br/>";
#     $data[$num]['date'] = $values[0];
#     $data[$num]['time'] = $values[1];
#     $data[$num]['mac']  = $values[2];
#     $data[$num]['site'] = $values[3];
#     $num++;
#   }
#   print $data[2]['mac']."<br/>";

    print "<br/>";
print <<eof;
          <h2 class="sub-header">Visit History</h2>
            <div class="table-responsive">
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Mac Address</th>
                    <th>Website</th>
                  </tr>
                </thead>
                <tbody>
eof
            # put it in reverse chron order
            @knownMacs;
            @lines = reverse @lines;
            my $num = 1;
            foreach my $line (@lines) {
              @values = split ' ', $line;
              print "<tr>";
              print "<td>$num</td>";
              # Date
              print "<td>$values[0]</td>";
              # Time
              print "<td>$values[1]</td>";
              # Mac
              print "<td>$values[2]</td>";
              my $mac = $values[2];
              push @knownMacs, $mac unless grep(/$mac/, @knownMacs);
              # Website
              print "<td>$values[3]</td>";
              print "</tr>";
              $num++;
            }

            if (defined param('blacklist1')) {
              # open or create blacklist file
              open BL, ">>", "blacklist.txt" or die "Cant open file $!";
              print BL "$knownMacs[0] ".param('blacklistText1')."\n";
              print "<h3 style='color:red;'>Successful blacklist: Please Reload Page</h3>";
            } elsif (defined param('blacklist2')) {
              open BL, ">>", "blacklist.txt" or die "Cant open file $!";
              print BL "$knownMacs[1] ".param('blacklistText2')."\n";
              print "<h3 style='color:red;'>Successful blacklist: Please Reload Page</h3>";
            }



            print <<eof;
                </tbody>
              </table>
            </div>


            <h1 class="page-header">Dashboard</h1>

            <div class="row placeholders">
              <div class="col-xs-6 col-sm-6 placeholder">
                <img src="/img/kid1.jpg" width="200" height="300" alt="Person 2">
                <h4>Richard</h4>
                <span class="text-muted">$knownMacs[0]</span>
        <form class="form" method="POST" action="">
        <input type="text" class="form-control" name="blacklistText1" id="blacklistText1" placeholder="Enter Domain To Blacklist">
        <button class="btn btn-danger" name="blacklist1" value="blacklist1">Blacklist</button>
        </form>
              </div>
              <div class="col-xs-6 col-sm-6 placeholder">
                <img src="/img/kid2.png" width="200" height="300" alt="Person 2">
                <h4>Joshua</h4>
                <span class="text-muted">$knownMacs[1]</span>
              <form class="form" method="POST" action="">
              <input type="text" class="form-control" name="blacklistText2" id="blacklistText2" placeholder="Enter Domain To Blacklist">
              <button class="btn btn-danger" name="blacklist2" value="blacklist2">Blacklist</button>
              </form>
              </div>
            </div>
eof
print <<eof;
          <h2 class="sub-header" style='color:red;'>BLACKLIST</h2>
            <div class="table-responsive">
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>MAC Address</th>
                    <th>Website</th>
                  </tr>
                </thead>
                <tbody>
eof
            open F, '<',"blacklist.txt";
            @lines = <F>;
            my $num = 1;
            foreach my $line (@lines) {
              @values = split ' ', $line;
              print "<tr>";
              print "<td>$num</td>";
              # MAC
              print "<td>$values[0]</td>";
              # Time
              print "<td>$values[1]</td>";
              my $mac = $values[2];
              push @knownMacs, $mac unless grep(/$mac/, @knownMacs);
              # Website
              print "<td>$values[3]</td>";
              print "</tr>";
              $num++;
            }
      print <<eof

          </div>
        </div>
      </div>
    </body>
  </html>
eof
}
main();