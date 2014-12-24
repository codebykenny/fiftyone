fifty.controller('BlogPost', ['$scope', '$http', '$location', '$routeParams',
	function ($scope, $http, $location, $routeParams) {
		$scope.id = $routeParams.id;
	}]);