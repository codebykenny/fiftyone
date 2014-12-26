fifty.controller('BlogCategory', ['$scope', '$http', '$location', '$routeParams',
	function ($scope, $http, $location, $routeParams) {
		$scope.category = $routeParams.id;
		$scope.posts = [];

		$http.get('/api/category/' + $scope.category).success(function (data) {
			for (var i in data) {
				data[i].fields.id = data[i].pk
				$scope.posts.push(data[i].fields)
			}
		});
	}]);