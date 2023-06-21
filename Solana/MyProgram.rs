// define the state of a program
use solana_program::program_pack::{IsInitialized, Sealed};
use arrayref::{array_mut_ref, array_ref, array_refs, mut_array_refs};

pub struct MyProgram {
    is_initialized: bool,
    data: u64,
}

impl Sealed for MyProgram {}

impl IsInitialized for MyProgram {
    fn is_initialized(&self) -> bool {
        self.is_initialized
    }
}

impl solana_program::program_pack::Pack for MyProgram {
    const LEN: usize = 9;
    fn unpack_from_slice(src: &[u8]) -> Result<Self, solana_program::program_error::ProgramError> {
        let src = array_ref![src, 0, MyProgram::LEN];
        let (
            is_initialized,
            data,
        ) = array_refs![src, 1, 8];
        let is_initialized = match is_initialized {
            [0] => false,
            [1] => true,
            _ => return Err(solana_program::program_error::ProgramError::InvalidAccountData),
        };
        Ok(MyProgram {
            is_initialized,
            data: u64::from_le_bytes(*data),
        })
    }

    fn pack_into_slice(&self, dst: &mut [u8]) {
        let dst = array_mut_ref![dst, 0, MyProgram::LEN];
        let (
            is_initialized_dst,
            data_dst,
        ) = mut_array_refs![dst, 1, 8];
        let &MyProgram {
            is_initialized,
            data,
        } = self;
        is_initialized_dst[0] = is_initialized as u8;
        *data_dst = data.to_le_bytes();
    }
}
