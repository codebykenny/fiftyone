fifty.controller('Home', ['$scope', '$http', '$location',
	function ($scope, $http, $location) {

		$scope.latest = [];

		$scope.categories = [{
			name: 'All'
		}, {
			name: 'Music'
		}];

		$scope.posts = [{
			id: 1,
			image: 'http://picture-cdn.wheretoget.it/impf1y-i.jpg',
			title: 'Back in Black'
		}, {
			id: 2,
			image: 'https://cdn.ticketfly.com/wp-content/themes/dougfirlounge/images/bg-venue-new.jpg',
			title: 'Top Venues This Month'
		},{
			id: 3,
			image: 'http://i.imgur.com/2nCk83R.jpg',
			title: 'Sony MDR-V6 Review'
		},{
			id: 1,
			image: 'http://blogs-images.forbes.com/hughmcintyre/files/2014/11/Pitbull.jpg',
			title: 'How is Pitbull So Famous?'
		}, {
			id: 2,
			image: 'http://the305.com/blog/wp-content/uploads/2013/04/DSC_0054.jpg',
			title: 'Ms. Cheezious - Queen of Food Trucks'
		},{
			id: 3,
			image: 'http://urbantastebuds.com/wp-content/uploads/2014/02/credit-cards-ftr.jpg',
			title: 'Shop Til\' You Drop Mayhem'
		}];

		$http.get('/api/latest/').success(function(data) {
			for (var i in data) {
				data[i].fields.id = data[i].pk
				$scope.latest.push(data[i].fields);
			}
		});

	}]);