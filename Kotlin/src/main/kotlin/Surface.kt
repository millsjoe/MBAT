import kotlin.math.roundToInt
/**
 * Performs initial operations on environment by marking
 * the border and placing the first cell. 
 * 
 * @property surface The environment (matrix) to use
 */
class Surface(private val surface: Array<IntArray>) {
    private val maxAmount: Int = surface.size - 1

    init {
        this.markABorder()
        this.centralCell()
    }
    /**
     * Marks the border with 2's.
     */
    private fun markABorder() {

        for (i in 0..maxAmount) {
            surface[0][i] = 2
            surface[maxAmount][i] = 2
            surface[i][0] = 2
            surface[i][maxAmount] = 2
            surface[maxAmount][maxAmount] = 2
        }
    }
    /**
     * Marks the initial cell in the middle of the matrix.
     */
    private fun centralCell() {
        val central = surface.size.toFloat() / 2
        surface[central.roundToInt()][central.roundToInt()] = 1
    }



}