@Suppress("NAME_SHADOWING")
/**
 * Begins diffusion when created as an instance.
 * 
 * @property surface The environment being used
 * @property initialCell The initial cell for the first walker
 * @property counterLimit Amount of diffusable cells
 */
class Diffuse( val surface: Array<IntArray>, initialCell: Pair<Int,Int>, counterLimit: Int) {

    private val cellClass = Cell(surface)
    private val counterLimit = counterLimit
    var finalArray: ArrayList<Array<IntArray>> = arrayListOf()
    init {
        diffuse(initialCell, 0)
    }

    /**
     *  Override toString to return the content of array
     * rather than its reference
     * 
     * @return String actual content
     */
    override fun toString(): String {
        return surface.contentDeepToString()
    }

    /**
     * Checks surrounding neighbours to determine if it is diffused 
     * or too close to the boundary
     * 
     * @param location Current location to check against
     * @return Pair(nextToNeighbour,nextToEdge) Boolean values to verify if next to boundary or next to diffused cell
     * 
     */
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

    /**
     * Decides the new random location to move to 
     * as one step.
     * 
     * @param location current location of cell
     * @return Pair(newX,newY) New x,y location of the cell
     */
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
    /**
     * Performs the diffusion. Recursively diffuses until either
     * the limit is met or the correct amount of cells have diffused
     * 
     * @param location Current location of cell
     * @param counter The current value of the counter to determine a return
     * 
     */
    private fun diffuse(location: Pair<Int, Int>, counter: Int) {
        var counter = counter
        counter++


        if (counter > counterLimit) return
        var location = location
        var neighbours = checkNeighbours(location)
        var cellDiffused = neighbours.first
        var tooCloseToEdge = neighbours.second

        while( !cellDiffused ) {
            if (tooCloseToEdge) {
                location = cellClass.randomCell()
            }
            location = randomlyMove(location)

            neighbours = checkNeighbours(location)
            cellDiffused = neighbours.first
            tooCloseToEdge = neighbours.second

        }

        val newArray: Array<IntArray> = surface.deepCopyIt()
        finalArray.add(newArray)
        surface[location.first][location.second] = 1

        diffuse(cellClass.randomCell(), counter)

    }
    /**
     * Takes a 2D-array and allows the contents to be copied
     * to a new one. Ensures there is no link with the given object.
     */
    private fun Array<IntArray>.deepCopyIt() = Array(size) { get(it).clone() }


}