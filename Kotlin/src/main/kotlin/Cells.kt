/**
 *  Used to generate a random cell (i.e walker)
 * 
 * @property surface The environment (surface) to be used
 */
class Cell(surface: Array<IntArray>){

    val maxAmount = surface.size - 1

    /**
     * Generates a random x & y on the surface
     * 
     * @return Pair containting x,y location
     */
    fun randomCell(): Pair<Int,Int> {
        val randomX = (1..maxAmount).random()
        val randomY = (1..maxAmount).random()
        return Pair(randomX,randomY)
    }
}