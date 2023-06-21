use thiserror::Error;

#[derive(Error, Debug, Copy, Clone)]
pub enum MyProgramError {
    #[error("Invalid Instruction")]
    InvalidInstruction,
}

impl From<MyProgramError> for ProgramError {
    fn from(e: MyProgramError) -> Self {
         ProgramError::Custom(e as u32)
    }
}
