pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let first_account = next_account_info(accounts_iter)?;

    match instruction_data[0] {
        0 => {
            let mut my_program = MyProgram::unpack_unchecked(&first_account.data.borrow())?;
            if my_program.is_initialized() {
                return Err(ProgramError::AccountAlreadyInitialized);
            }
            my_program.is_initialized = true;
            my_program.pack_into_slice(&mut first_account.data.borrow_mut());
        }
        _ => return Err(ProgramError::InvalidInstructionData),
    }
    Ok(())
}
