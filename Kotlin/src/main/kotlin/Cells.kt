class Cell(surface: Array<IntArray>){

    val maxAmount = surface.size - 1
    fun randomCell(): Pair<Int,Int> {
        val randomX = (1..maxAmount).random()
        val randomY = (1..maxAmount).random()
        return Pair(randomX,randomY)
    }
}