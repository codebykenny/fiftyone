var fifty=angular.module('fifty',['ngRoute']).config(['$routeProvider','$locationProvider',function($routeProvider,$locationProvider){$routeProvider.when('/logout',{templateUrl:'/views/login/index',controller:'Logout'}).when('/:controller/:action/:id',{templateUrl:function(params){return'/views/'+params.controller+'/'+params.action;},controller:function($scope,$routeParams,$controller,$location,$window){var controller,action,nameRegEx=/(^|_)([a-z])/g;controller=$routeParams.controller.replace(nameRegEx,function(){return arguments[2].toUpperCase();});action=$routeParams.action.replace(nameRegEx,function(){return arguments[2].toUpperCase();});$controller(controller+action,{$scope:$scope});}}).when('/:controller/:action',{templateUrl:function(params){return'/views/'+params.controller+'/'+params.action;},controller:function($scope,$routeParams,$controller,$location,$window){var controller,action,nameRegEx=/(^|_)([a-z])/g;controller=$routeParams.controller.replace(nameRegEx,function(){return arguments[2].toUpperCase();});action=$routeParams.action.replace(nameRegEx,function(){return arguments[2].toUpperCase();});$controller(controller+action,{$scope:$scope});}}).when('/:controller',{templateUrl:function(params){return'/views/'+params.controller+'/index';},controller:function($scope,$routeParams,$controller,$location,$window){var controller,nameRegEx=/(^|_)([a-z])/g;controller=$routeParams.controller.replace(nameRegEx,function(){return arguments[2].toUpperCase();});$controller(controller,{$scope:$scope});}}).when('/',{templateUrl:'/views/home/index',controller:'Home'}).otherwise({templateUrl:'/views/error/404',controller:function(){}});$locationProvider.html5Mode(true);}]).directive('setBlogBackground',['$http','$timeout',function($http,$timeout){return{restrict:'A',link:function(scope,element,attrs){$timeout(function(){element.css('background','linear-gradient(rgba(198, 198, 198, 0.45), rgba(17, 17, 17, 0.75)), url('+attrs.image+')');element.css('background-position','center center');},0);}};}]);;fifty.controller('Home',['$scope','$http','$location',function($scope,$http,$location){$scope.latest=[];$scope.categories=[{name:'All'},{name:'Music'}];$scope.posts=[{id:1,image:'http://picture-cdn.wheretoget.it/impf1y-i.jpg',title:'Back in Black'},{id:2,image:'https://cdn.ticketfly.com/wp-content/themes/dougfirlounge/images/bg-venue-new.jpg',title:'Top Venues This Month'},{id:3,image:'http://i.imgur.com/2nCk83R.jpg',title:'Sony MDR-V6 Review'},{id:1,image:'http://blogs-images.forbes.com/hughmcintyre/files/2014/11/Pitbull.jpg',title:'How is Pitbull So Famous?'},{id:2,image:'http://the305.com/blog/wp-content/uploads/2013/04/DSC_0054.jpg',title:'Ms. Cheezious - Queen of Food Trucks'},{id:3,image:'http://urbantastebuds.com/wp-content/uploads/2014/02/credit-cards-ftr.jpg',title:'Shop Til\' You Drop Mayhem'}];$http.get('/api/latest/').success(function(data){for(var i in data){data[i].fields.id=data[i].pk
$scope.latest.push(data[i].fields);}});}]);fifty.controller('BlogPost',['$scope','$http','$location','$routeParams',function($scope,$http,$location,$routeParams){$scope.id=$routeParams.id;$http.get('/api/post/'+$scope.id).success(function(data){$scope.post=data[0].fields;$scope.post.created=Date.parse($scope.post.created);$scope.author={};$scope.author.name=$scope.post.author[0]
$scope.author.image_url=$scope.post.author[1]
console.log($scope.post.created)});}]);fifty.controller('BlogCategory',['$scope','$http','$location','$routeParams',function($scope,$http,$location,$routeParams){$scope.category=$routeParams.id;$scope.posts=[];$http.get('/api/category/'+$scope.category).success(function(data){for(var i in data){data[i].fields.id=data[i].pk
$scope.posts.push(data[i].fields)}});}]);