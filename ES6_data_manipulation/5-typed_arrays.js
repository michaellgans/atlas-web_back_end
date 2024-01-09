/* Task 5 */

export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(1);
  const dataView = new DataView(buffer);
  dataView.setInt8(position, value);

  return buffer;
}
