export default function getNeighborhoodsList() {
  /* Origional List */
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  /* Creates a function called addNeighborhood that takes in a
  a variable called newNeighborhood */
  this.addNeighborhood = (newNeighborhood) => {
    /* Appends newNeighborhood into list */
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    return this.sanFranciscoNeighborhoods;
  };
}
