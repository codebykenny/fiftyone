var fifty = angular.module('fifty', [
		'ngRoute'
	])

	.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
		$routeProvider
			.when('/logout', {
				templateUrl: '/views/login/index',
				controller: 'Logout'
			})
			.when('/:controller/:action/:id', {
				templateUrl: function (params) {
					return '/views/' + params.controller + '/' + params.action;
				},
				controller: function ($scope, $routeParams, $controller, $location, $window) {
					var controller, action,
						nameRegEx = /(^|_)([a-z])/g;

						controller = $routeParams.controller.replace(nameRegEx, function () {
							return arguments[2].toUpperCase();
						});

						action = $routeParams.action.replace(nameRegEx, function () {
							return arguments[2].toUpperCase();
						});

						$controller(controller + action, {$scope: $scope});
					}
			})
			.when('/:controller/:action', {
				templateUrl: function (params) {
					return '/views/' + params.controller + '/' + params.action;
				},
				controller: function ($scope, $routeParams, $controller, $location, $window) {
					var controller, action,
						nameRegEx = /(^|_)([a-z])/g;

						controller = $routeParams.controller.replace(nameRegEx, function () {
							return arguments[2].toUpperCase();
						});

						action = $routeParams.action.replace(nameRegEx, function () {
							return arguments[2].toUpperCase();
						});

						$controller(controller + action, {$scope: $scope});
					}
			})
			.when('/:controller', {
				templateUrl: function (params) {
					return '/views/' + params.controller + '/index';
				},
				controller: function ($scope, $routeParams, $controller, $location, $window) {
					var controller,
						nameRegEx = /(^|_)([a-z])/g;

					controller = $routeParams.controller.replace(nameRegEx, function () {
						return arguments[2].toUpperCase();
					});

					$controller(controller, {$scope: $scope});
				}
			})
			.when('/', {
				templateUrl: '/views/home/index',
				controller: 'Home'
			})
			.otherwise({
				templateUrl: '/views/error/404',
				controller: function () {}
			});

			$locationProvider.html5Mode(true);
	}])

	.directive('setBlogBackground', ['$http',  '$timeout', function ($http, $timeout) {
		return {
			restrict: 'A',
			link: function (scope, element, attrs) {
				$timeout(function() {
					element.css('background', 'linear-gradient(rgba(198, 198, 198, 0.45), rgba(17, 17, 17, 0.75)), url(' + attrs.image + ')');
					element.css('background-position', 'center center');
				}, 0);
			}
		};
	}]);

;