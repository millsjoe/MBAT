/**
 * Translates a matrix into a JSON compatible string.
 * 
 * @property modelArray 2D array of the environment
 */
class Model(private val modelArray: Array<IntArray>) {
    /**
     * Overwrites toString to give the correct format for JSON
     * 
     * @return String JSON formatted string
     */
    override fun toString(): String {
        return "Category [modelArray: ${this.modelArray}]"
    }
}
