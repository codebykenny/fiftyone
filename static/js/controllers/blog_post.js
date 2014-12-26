fifty.controller('BlogPost', ['$scope', '$http', '$location', '$routeParams',
	function ($scope, $http, $location, $routeParams) {
		$scope.id = $routeParams.id;

		$http.get('/api/post/' + $scope.id).success(function (data) {

			$scope.post = data[0].fields;
			$scope.post.created = Date.parse($scope.post.created);

			$scope.author = {};
			$scope.author.name = $scope.post.author[0]
			$scope.author.image_url = $scope.post.author[1]
			console.log($scope.post.created)
		});

	}]);