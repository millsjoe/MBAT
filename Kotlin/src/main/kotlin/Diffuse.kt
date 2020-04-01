class Diffuse(private val surface: Array<IntArray>, initialCell: Pair<Int,Int>, counterLimit: Int) {

    private val cellClass = Cell(surface)
    private val counterLimit = counterLimit

    private fun checkNeighbours(location: Pair<Int,Int>): Pair<Boolean, Boolean> {
        var nextToNeighbour = false
        var nextToEdge = false

        val maxAmount = cellClass.maxAmount

        val left = Pair(location.first - 1,location.second)
        val right = Pair(location.first + 1,location.second)
        val up = Pair(location.first,location.second - 1)
        val down = Pair(location.first,location.second + 1)

        when {
            left.first < 0  -> nextToEdge = true
            right.first > maxAmount -> nextToEdge = true
            up.second < 0 -> nextToEdge = true
            down.second > maxAmount -> nextToEdge = true
        }
        if (!nextToEdge) {
            if ( surface[left.first][left.second] == 1 ||
                surface[right.first][right.second] == 1 ||
                surface[up.first][up.second] == 1 ||
                surface[down.first][down.second] == 1 )
            {
                nextToNeighbour = true
            }


        }

        return Pair(nextToNeighbour,nextToEdge)
    }

    private fun randomlyMove(location: Pair<Int, Int>): Pair<Int,Int> {
        val direction = (0..3).random()
        var newX = location.first
        var newY = location.second
        when (direction) {
            0 -> newX = location.first + 1
            1 -> newX = location.first - 1
            2 -> newY = location.second + 1
            3 -> newY = location.second - 1
        }
        return Pair(newX,newY)
    }
