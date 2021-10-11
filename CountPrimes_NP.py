
from timeit import default_timer
import numpy as np


class PrimeCounter:

    _size   :int
    _bits   :np.array


    VALID_PRIMES :dict = { 10 : 4,
                          100 : 25,
                        1_000 : 168,
                       10_000 : 1_229,
                      100_000 : 9_592,
                    1_000_000 : 78_498,
                   10_000_000 : 664_579,
                  100_000_000 : 5_761_455 };




    def __init__( self, pool_size:int ) -> None:
        self._size = pool_size;
        self._bits = np.ones( ( ( self._size +1 ) //2 ), dtype=np.bool_ );





    def countPrimes( self ) -> int :
        return sum( self._bits );





    def getPrimes( self ) -> np.array:                              # Return numpy array of all prime values
        return np.where( self._bits )[ 0 ] *2 +1;





    def runSieve( self ) -> None:                                   # Toggle all non-primes in "_bit" array

        START_INDEX = 3;                                            # Initializes with primes 2/3/5 preset 
        STEP_SIZE   = 2;                                            # Increments by 2 to skip even numbers
        MAX_LENGTH  = int( np.sqrt( self._size ) ) +1;              # Prevents excess loop indicies

        for index in range( START_INDEX, MAX_LENGTH, STEP_SIZE ):
            if( self._bits[ index //2 ] ):                          # Check Bit
                self._bits[ int( index *1.5 ) :: index ] = False;   # Clear Bit





    def validatePrimes( self ) -> bool:                             # Confirm the number of found primes against known primes
        if( self._size in self.VALID_PRIMES ):
            return self.countPrimes( ) == self.VALID_PRIMES[ self._size ];
        return False;





    def printf( self, ET:float, PASSES:int ) -> None:
        
        b_result = self.validatePrimes( );
        if( not b_result ): print( 'RESULTS UNCONFIRMED' );
        print('PASSES:{P}, ELAPSED TIME:{E}, AVG:{A}, LIMIT:{L}, COUNT:{C}, Valid:{V}'.format( P=PASSES, E=ET, A=ET/PASSES, L=self._size, C=self.countPrimes( ), V=b_result ) );





if __name__ == '__main__':
    ELAPSED_TIME = lambda START_TIME: default_timer( ) -START_TIME;


    START_TIME = default_timer( );          # <- Begin timer!!

    numer_of_passes :int = 0;
    while( ELAPSED_TIME( START_TIME ) < 5 ):
        PC = PrimeCounter( 1_000_000 );
        PC.runSieve( );
        numer_of_passes +=1;

    ET = ELAPSED_TIME( START_TIME );        # <- End timer!!


    PC.printf( ET, numer_of_passes );
