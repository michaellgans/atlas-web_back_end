-- Task 8: Creates an idex based on the first letter
-- of a name
CREATE INDEX idx_name_first ON names ((LEFT(name, 1)));
