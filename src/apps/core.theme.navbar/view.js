let wiz_controller = async ($sce, $scope, $timeout) => {
    $scope.branch = {};
    $scope.branch.id = wiz.data.BRANCH;
    $scope.branch.list = wiz.data.BRANCHES;
    $scope.branch.change = async (branchname) => {
        location.href = location.pathname + "?branch=" + branchname;
    }
};